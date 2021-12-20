from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    email = fields.CharField(max_length=120, unique=True)
    password = fields.CharField(max_length=20)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)
    professions = fields.ManyToManyField('models.Profession', related_name='users')


User_Pydantic = pydantic_model_creator(User, name='User', exclude=('password',))
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
