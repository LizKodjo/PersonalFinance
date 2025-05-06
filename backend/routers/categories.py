from bson import ObjectId
from fastapi import APIRouter, Depends, Form, Request, status
from authentication import AuthHandler
from models import CategoryModel

router = APIRouter()
auth_handler = AuthHandler()


@router.post("/", response_description="Add a category", response_model=CategoryModel, status_code=status.HTTP_201_CREATED, response_model_by_alias=False)
async def add_category(request: Request, name: str = Form("name"), transaction: str = Depends(auth_handler.auth_wrapper)):
    category = CategoryModel(
        name=name,
        transaction_id=transaction["transaction_id"],
    )
    categories = request.app.db["categories"]
    document = category.model_dump(by_alias=True, exclude=["id"])
    inserted = await categories.insert_one(document)

    return await categories.find_one({"_id": inserted.inserted_id})
