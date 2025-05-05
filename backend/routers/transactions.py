from bson import ObjectId
from fastapi import APIRouter, Body, Depends, Form, HTTPException, Request, status
from fastapi.responses import Response
from pymongo import ReturnDocument
from models import TransactionModel, ListTransactions, UpdateTransactionModel, TransactionCollectionPagination
from authentication import AuthHandler

router = APIRouter()
TRANSACTIONS_PER_PAGE = 10
auth_handler = AuthHandler()


@router.post("/", response_description="Add a transaction", response_model=TransactionModel, status_code=status.HTTP_201_CREATED, response_model_by_alias=False)
async def add_transaction(request: Request, type: str = Form("type"), amount: float = Form("amount"), category: str = Form("category"), date: str = Form("date"), description: str = Form("description"), user: str = Depends(auth_handler.auth_wrapper),):
    transaction = TransactionModel(
        type=type,
        amount=amount,
        category=category,
        date=date,
        description=description,
        user_id=user["user_id"],
    )
    transactions = request.app.db["transactions"]
    document = transaction.model_dump(by_alias=True, exclude=["id"])
    inserted = await transactions.insert_one(document)

    return await transactions.find_one({"_id": inserted.inserted_id})


# @router.get("/", response_description="List all transactions", response_model=ListTransactions, response_model_by_alias=False)
# async def list_transactions(request: Request):
#     transactions = request.app.db["transactions"]
#     results = []
#     cursor = transactions.find()
#     async for document in cursor:
#         results.append(document)

#     return ListTransactions(transactions=results)

@router.get("/", response_description="List all transactions, paginated", response_model=TransactionCollectionPagination, response_model_by_alias=False,)
async def list_transactions(request: Request, page: int = 1, limit: int = TRANSACTIONS_PER_PAGE,):
    transactions = request.app.db["transactions"]
    results = []
    cursor = transactions.find().sort("companyName").limit(
        limit).skip((page - 1) * limit)
    total_documents = await transactions.count_documents({})
    has_more = total_documents > limit * page
    async for document in cursor:
        results.append(document)
    return TransactionCollectionPagination(transactions=results, page=page, has_more=has_more)


@router.get("/{id}", response_description="Get a single transaction", response_model=TransactionModel, response_model_by_alias=False,)
async def show_transaction(id: str, request: Request):
    transactions = request.app.db["transactions"]
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=404, detail=f"Transaction {id} not found")
    if (transaction := await transactions.find_one({"_id": ObjectId(id)})) is not None:
        return transaction
    raise HTTPException(
        status_code=404, detail=f"Transaction with {id} not found")


@router.put("/{id}", response_description="Update a transaction", response_model=UpdateTransactionModel, response_model_by_alias=False)
async def update_transaction(id: str, request: Request, user=Depends(auth_handler.auth_wrapper), transaction: UpdateTransactionModel = Body(...),):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=404, detail=f"Transaction {id} not found")

    transaction = {
        k: v
        for k, v in transaction.model_dump(by_alias=True).items()
        if v is not None and k != "_id"
    }
    if len(transaction) >= 1:
        transactions = request.app.db["transactions"]

        update_result = await transactions.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": transaction},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Car {id} not found")
    if (existing_transaction := await transactions.find_one({"_id": id})) is not None:
        return existing_transaction
    raise HTTPException(status_code=404, detail=f"Transaction {id} not found")


@router.delete("/{id}", response_description="Delete a transaction")
async def delete_transaction(id: str, request: Request, user=Depends(auth_handler.auth_wrapper)):
    try:
        id = ObjectId(id)
    except Exception:
        raise HTTPException(
            status_code=404, detail=f"Transaction {id} not found")
    transactions = request.app.db["transactions"]
    delete_result = await transactions.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=404, detail=f"Transaction with {id} not founx")
