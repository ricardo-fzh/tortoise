from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Profession(Model):
    name = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


Profession_pydantic = pydantic_model_creator(Profession, name='Profession')
ProfessionIn_pydantic = pydantic_model_creator(Profession, name='ProfessionIn', exclude_readonly=True)
