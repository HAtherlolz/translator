from fastapi import WebSocket
from main import app


from app.repositories.rooms import get_room


@app.websocket("/ws/{room_uuid}/{user_uuid}")
async def websocket_endpoint(websocket: WebSocket, room_uuid: str, user_uuid: str):
    await websocket.accept()

    room = await get_room(room_uuid)
    if not room:
        pass

    user_in_room = False
    for user in room.users:
        if user.uuid == user_uuid:
            user_in_room = True

    if not user_in_room:
        pass

