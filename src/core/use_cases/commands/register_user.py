from src.core.domain.repositories.user_repository_interface import UserRepositoryInterface
from src.schemas.user_schema import UserCreateSchema
from src.core.domain.models.user import User
import datetime

class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, command: UserCreateSchema) -> User:
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
        saved_user = self.user_repository.save(new_user)
        return saved_user