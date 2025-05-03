from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/")
def userTest():
    return "User endpoint"
