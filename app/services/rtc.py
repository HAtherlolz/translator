from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer, MediaRecorder


class WebRTCConnection:
    def __init__(self, websocket):
        self.websocket = websocket
        self.pc = RTCPeerConnection()
        self.pc.addTransceiver("audio")
        self.pc.addTransceiver("video")

        @self.pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            print("ICE connection state is", self.pc.iceConnectionState)
            if self.pc.iceConnectionState == "failed":
                await self.websocket.close()

        @self.pc.on("track")
        async def on_track(track):
            print("Track received:", track.kind)
            if track.kind == "audio":
                self.audio = track
            elif track.kind == "video":
                self.video = track

        @self.pc.on("icecandidate")
        async def on_icecandidate(candidate):
            await self.websocket.send_json(
                {"type": "candidate", "candidate": candidate}
            )

    async def handle_sdp(self, data):
        await self.pc.setRemoteDescription(
            RTCSessionDescription(sdp=data["sdp"], type=data["type"])
        )
        if data["type"] == "offer":
            await self.pc.setLocalDescription(await self.pc.createAnswer())
            await self.websocket.send_json(
                {
                    "res_type": "answer",
                    "sdp": self.pc.localDescription.sdp,
                    "type": self.pc.localDescription.type,
                }
            )

    async def handle_candidate(self, data):
        await self.pc.addIceCandidate(data["candidate"])
