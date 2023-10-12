from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from uuid import uuid4, UUID


class Status(str, Enum):
    LOCK = "LOCK"
    ACTIVE = "ACTIVE"


class Role(str, Enum):
    USER = "USER"
    EMPLOYER = "EMPLOYER"
    ADMIN = "ADMIN"


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    login: str = Field(min_length=8, max_length=16)
    email: EmailStr
    first_name: str = Field(min_length=2, max_length=24, )
    mid_name: str = Field(min_length=2, max_length=24)
    last_name: str = Field(min_length=2, max_length=24)
    phone: str = Field(min_length=3, max_length=12)
    role: Role
    status: Status


class ApiKeys(BaseModel):
    key: str
