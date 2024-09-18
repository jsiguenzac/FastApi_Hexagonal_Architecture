from src.schemas.user_schema import UserCreateSchema, UserFindSchema
from src.core.use_cases.commands.register_user import  RegisterUserUseCase
from src.core.use_cases.queries.get_user_by_id import GetUserByIdUseCase
from src.adapters.repositories.user_repository import UserRepository
from src.config.database import get_db
from src.utils.helpers import exit_json

db = next(get_db())

class UserService:
    def __init__(self, db_session=db):
        self.user_repository = UserRepository(db_session)

    async def register_user(self, data_user: UserCreateSchema):
        try:
            use_case = RegisterUserUseCase(self.user_repository)
            user = await use_case.execute(data_user)
            print(user)
            if user is None:
                return exit_json(0, {
                    "exito": False,
                    "mensaje": "ERROR_REGISTRO_USUARIO"
                })
            return exit_json(1, {
                "exito": True,
                "user_id": user.idUsuario,
                "mensaje": "USUARIO_REGISTRADO"
            })
        except Exception as e:
            return exit_json(0, {
                "exito": False,
                "mensaje": str(e)
            })

    async def get_user_by_id(self, user_id: int):
        try:
            use_case = GetUserByIdUseCase(self.user_repository)
            user = await use_case.execute(user_id)
            
            if user is None:
                return exit_json(0, {"mensaje": "USUARIO_NO_ENCONTRADO"})
            
            if not user.Activo:
                return exit_json(0, {"mensaje": "USUARIO_INACTIVO"})

            # uso de UserFindSchema
            user_map = UserFindSchema(
                id_user=user.idUsuario,
                name=user.Nombre,
                last_name=user.Apellidos,
                email=user.Correo,
                phone=user.Telefono
            )
            return exit_json(1, user_map)
        except Exception as e:
            return exit_json(0, {"mensaje": str(e)})