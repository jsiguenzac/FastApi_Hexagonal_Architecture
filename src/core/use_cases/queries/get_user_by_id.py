from src.core.domain.repositories.user_repository_interface import UserRepositoryInterface
from src.core.domain.models.user import User

""" class GetUserByIdQuery:
    def __init__(self, user_id: int):
        self.user_id = user_id """

class GetUserByIdUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        user = await self.user_repository.get_by_id(user_id)
        return user