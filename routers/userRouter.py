from typing import List
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from models.userModel import User_Pydantic, UserIn_Pydantic, User
from controller.userController import get_all, create, delete
from schemas.statusSchema import Status

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('/', response_model=List[User_Pydantic])
async def get_user_all():
    return await get_all(User, User_Pydantic)


@router.post('/create', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    return await  create(User, user, User_Pydantic)


@router.delete('/delete/{user_id}', response_model=Status, responses={404: {'model': HTTPNotFoundError}})
async def delete_user(user_id: int):
    return await delete(User, user_id, Status)
