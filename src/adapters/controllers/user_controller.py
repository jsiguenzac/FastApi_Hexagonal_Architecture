from fastapi import APIRouter, HTTPException, status
from src.schemas.user_schema import UserCreateSchema
from src.adapters.services.user_service import UserService

router = APIRouter(
    prefix="/User",
    tags=["Usuarios"]
)

service = UserService()

@router.post("/Register", status_code=status.HTTP_201_CREATED)
async def register_user(data_user: UserCreateSchema):
    user = await service.register_user(data_user)
    return user

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    user = await service.get_user_by_id(user_id)
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user