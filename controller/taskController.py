async def get_task(task_pydantic, task):
    return await task_pydantic.from_queryset(task.all())


async def create(task_pydantic, task_model, task_list_pydantic):
   new_task = await task_model.create(**task_pydantic.dict(exclude_unset=True))
   return await task_list_pydantic.from_tortoise_orm(new_task)