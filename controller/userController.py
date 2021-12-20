from fastapi import HTTPException, status


async def get_all(user, user_pydantic):
    return await user_pydantic.from_queryset(user.all())


async def create(user_model, user, user_pydantic):
    new_user = await user_model.create(**user.dict(exclude_unset=True))
    return await user_pydantic.from_tortoise_orm(new_user)


async def delete(user, user_id, status):
    user_db = await  user.filter(id=user_id).delete()
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")

    return status(message=f'Deleted user {user_id}')

