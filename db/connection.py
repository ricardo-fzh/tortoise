from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

def get_connection(app):

    register_tortoise(
        app,
        db_url='postgres://postgres:admin@localhost:5432/symlab',
        modules={'models': ['models.taskModel', 'models.userModel', 'models.professionModel']},
        generate_schemas=False,
        add_exception_handlers=True
    )

    Tortoise.init_models(["__main__"], "models")
