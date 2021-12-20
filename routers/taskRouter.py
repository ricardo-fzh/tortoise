from typing import List
from fastapi import  APIRouter
from  models.taskModel import TaskIn_Pydantic, Task_Pydantic, Task
from controller.taskController import get_task, create

router = APIRouter(
    prefix='/task',
    tags=['task']
)

@router.get('/', response_model=List[Task_Pydantic])
async def get_all_tasks():
    return await get_task(Task_Pydantic, Task)

@router.post('/create', response_model=Task_Pydantic)
async def create_task(task: TaskIn_Pydantic):
    return await create(task, Task, Task_Pydantic)