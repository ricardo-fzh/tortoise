from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class Task(Model):
    name = fields.CharField(max_length=120)
    description = fields.TextField()
    users = fields.ForeignKeyField("models.User", related_name='tasks')

    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)



Task_Pydantic = pydantic_model_creator(Task, name='Task')
TaskIn_Pydantic = pydantic_model_creator(Task, name='TaskIn',  exclude_readonly=True)



