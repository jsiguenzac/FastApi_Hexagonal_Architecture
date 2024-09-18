from src.core.domain.repositories.user_repository_interface import UserRepositoryInterface
from src.core.domain.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def save(self, user: User) -> User:
        self.db_session.add(user)
        self.db_session.commit()
        return user

    async def get_by_id(self, user_id: int) -> User:
        return self.db_session.get(User, user_id)