from datetime import datetime
from pydantic import BaseModel, EmailStr

from application.api.schemas import SBaseQueryResponse
from domain.entities.users import UserEntity


class SCreateUserIn(BaseModel):
    email: EmailStr
    username: str
    password: str
    is_subscribed: bool = False


class SCreateUserOut(BaseModel):
    oid: str
    email: EmailStr
    username: str
    created_at: datetime
    is_subscribed: bool

    @classmethod
    def from_entity(cls, user: UserEntity) -> "SCreateUserOut":
        return cls(
            oid=user.oid,
            email=user.email.as_generic_type(),
            username=user.username.as_generic_type(),
            created_at=user.created_at,
            is_subscribed=user.is_subscribed,
        )


class SLoginIn(BaseModel):
    username: str
    password: str


class SLoginOut(BaseModel):
    oid: str
    email: EmailStr
    username: str
    created_at: datetime
    is_subscribed: bool

    @classmethod
    def from_entity(cls, user: UserEntity) -> "SLoginOut":
        return cls(
            oid=user.oid,
            email=user.email.as_generic_type(),
            username=user.username.as_generic_type(),
            created_at=user.created_at,
            is_subscribed=user.is_subscribed,
        )


class SGetUser(BaseModel):
    oid: str
    email: EmailStr
    username: str
    created_at: datetime
    is_subscribed: bool

    @classmethod
    def from_entity(cls, user: UserEntity) -> "SGetUser":
        return cls(
            oid=user.oid,
            email=user.email.as_generic_type(),
            username=user.username.as_generic_type(),
            created_at=user.created_at,
            is_subscribed=user.is_subscribed,
        )


class SChangeUsername(BaseModel):
    new_username: str


class SChangePassword(BaseModel):
    old_password: str
    new_password: str


class SGetUsersQueryResponse(SBaseQueryResponse[list[SGetUser]]): ...
