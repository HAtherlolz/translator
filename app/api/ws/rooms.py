from fastapi import WebSocket, APIRouter


from app.repositories.rooms import get_room
from app.services.rtc import WebRTCConnection


ws_router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
        self.active_profiles: dict = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)

    async def send_message_to_profile(self, message: dict, profile_id: int):
        for client_ws, ws_profile_id in self.active_profiles.items():
            if ws_profile_id == profile_id:
                await client_ws.send_json(message)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

    async def append_active_profile(self, websocket: WebSocket, profile_id: str):
        self.active_profiles[websocket] = profile_id

    async def remove_active_profile(self, websocket: WebSocket):
        del self.active_profiles[websocket]


manager = ConnectionManager()


@ws_router.websocket("/ws/{room_uuid}/{user_uuid}/")
async def websocket_endpoint(websocket: WebSocket, room_uuid: str, user_uuid: str | None = None):
    # Connection
    await manager.connect(websocket)

    # room logic
    room = await get_room(room_uuid)
    if not room:
        pass

    print("Room", room)

    user_in_room = None

    for user in room.users:
        if user.uuid == user_uuid:
            user_in_room = user

    if not user_in_room:
        manager.disconnect(websocket)

    await manager.append_active_profile(websocket, user_in_room.uuid)
    await manager.send_personal_message(
        {
            "type": "INFO",
            "message": f"Connection successful"
        },
        websocket
    )

    connection = WebRTCConnection(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "offer" or data["type"] == "answer":
                await connection.handle_sdp(data)
            elif data["type"] == "candidate":
                await connection.handle_candidate(data)
    except Exception as e:
        print("WebRTC connection closed:", e)
