from db.connection import get_connection
from routers import userRouter, taskRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(userRouter.router)
app.include_router(taskRouter.router)


get_connection(app)
