from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from app.routers.message_router import router as message_router
from app.routers.user_router import router as user_router
from app.routers.websoc_router import router as websoc_router
from app.DB.connection import create_database
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


templates = Jinja2Templates(directory="app/templates")

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(message_router)
v1_router.include_router(user_router)


app = FastAPI(
    title="GRRN-Chatbox",
    description="A simple chat application",
    version="0.1",
    openapi_tags=[
        {
            "name": "messages",
            "description": "Operations with messages. The messages are the ones that are sent from one user to another."
        },
        {
            "name": "users",
            "description": "Operations with users. The users are the ones that are registered in the application."
        },
        {
            "name": "websockets",
            "description": "Operations with websockets. The websockets are the ones that are used to send and receive messages in real time."
        }
    ]
)


origins = ['*']
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{user_id}")
async def root(request: Request, user_id: int):
  return templates.TemplateResponse("test.html", {"request": request, "user_id": user_id})



app.include_router(websoc_router)
app.include_router(v1_router)

if __name__ == "__main__":
    create_database()
    uvicorn.run(app="main:app", port=8000, reload=True)
