from datetime import datetime
from typing import Optional, Annotated, List
from pydantic import BaseModel, ConfigDict, Field, BeforeValidator, field_validator

PyObjectId = Annotated[str, BeforeValidator(str)]


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    fullname: str = Field(...)
    email: str = Field(...)
    password1: str = Field(...)
    password2: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, json_schema_extra={
            "example": {
                "fullname": "Tom Jones",
                "email": "test@test.com",
                "password1": "password",
                "password2": "password"
            }
        }
    )


class UpdateUser(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password1: str = Field(...)
    password2: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, json_schema_extra={
            "example": {
                "fullname": "Tom Jones",
                "email": "test@test.com",
                "password1": "password",
                "password2": "password"
            }
        }
    )


class ListUsers(BaseModel):
    users: List[UserModel]


class TransactionModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    type: str = Field(...)
    amount: int = Field(..., gt=0, lt=100000)
    category: str = Field(...)
    date: str
    description: str

    @field_validator("category")
    def check_category_case(cls, v: str) -> str:
        return v.title()

    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, json_schema_extra={
            "example": {
                "type": "Incoming",
                "amount": 100.00,
                "category": "Food",
                "date": "3/5/2025",
                "description": "Hello testing"
            }
        }
    )


class ListTransactions(BaseModel):
    transactions: List[TransactionModel]


class UpdateTransactionModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    type: str = Field(...)
    amount: int = Field(..., gt=0, lt=100000)
    category: str = Field(...)
    date: str
    description: str

    @field_validator("category")
    def check_category_case(cls, v: str) -> str:
        return v.title()

    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, json_schema_extra={
            "example": {
                "type": "Incoming",
                "amount": 100.00,
                "category": "Food",
                "date": "3/5/2025",
                "description": "Hello testing"
            }
        }
    )


class TransactionCollectionPagination(ListTransactions):
    page: int = Field(ge=1, default=1)
    has_more: bool
