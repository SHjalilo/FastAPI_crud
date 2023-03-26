from pydantic import BaseModel


class employees(BaseModel):
    name:str
    age:int
    departement:str
