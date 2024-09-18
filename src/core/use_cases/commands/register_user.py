import datetime
from src.core.domain.repositories.user_repository_interface import UserRepositoryInterface
from src.schemas.user_schema import UserCreateSchema
from src.core.domain.models.user import User

""" class RegisterUserCommand:
    def __init__(self, user_data: UserCreateSchema):
        self.name = user_data.name
        self.last_name = user_data.last_name
        self.email = user_data.email
        self.password = user_data.password
        self.phone = user_data.phone """

class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    async def execute(self, command: UserCreateSchema) -> User:
        new_user = User(
            Nombre=command.name,
            Apellidos=command.last_name,
            Correo=command.email,
            Clave=command.password,
            Telefono=command.phone,
            Activo=True,
            FechaHoraCreacion=datetime.datetime.now(),
            UsuarioCreacion='Dev'
        )
        saved_user = await self.user_repository.save(new_user)
        return saved_user