from fastapi import APIRouter, WebSocket
from app.services.websocket_services import manager


router = APIRouter()
TYPING_TIMEOUT = 5

import time

@router.websocket("/ws/{receiver_id}")
async def websocket_endpoint(websocket: WebSocket, receiver_id: int):
  await manager.connect(websocket)
  last_received_time = time.time()
  try:
    while True:
      data = await websocket.receive_text()
      current_time = time.time()
      if current_time - last_received_time > TYPING_TIMEOUT:
        await manager.broadcast_typing_status(receiver_id, False)
      else:
        await manager.broadcast_typing_status(receiver_id, True)
      await manager.broadcast_message(receiver_id, data)  # Add this line
      last_received_time = current_time
  except Exception as e:
    print(e)
  finally:
    await manager.disconnect(websocket)