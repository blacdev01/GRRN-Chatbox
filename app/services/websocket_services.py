from fastapi import WebSocket


class WebSocketManager:
    def __init__(self):
        self.active_connections = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_typing_status(self, receiver_id: int, is_typing: bool):
        for connection in self.active_connections:
            
            await connection.send_json({"receiver_id": receiver_id, "is_typing": is_typing})
    
    async def broadcast_message(self, receiver_id: int, message: str):
        for connection in self.active_connections:
            await connection.send_json({"receiver_id": receiver_id, "message": message})


manager = WebSocketManager()