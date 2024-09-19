import unittest
from unittest.mock import Mock
from src.core.use_cases.commands.register_user import RegisterUserUseCase
from src.schemas.user_schema import UserCreateSchema
from src.core.domain.models.user import User
import datetime

class TestRegisterUserUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock()
        self.use_case = RegisterUserUseCase(self.mock_repository)
    
    def test_execute(self):
        # Datos de prueba
        command = UserCreateSchema(
            name="Joel",
            last_name="Sigüenza",
            email="siguenzajoel10@gamil.com",
            password="76411904",
            phone="921018664"
        )
        mock_user = User(
            Nombre=command.name,
            Apellidos=command.last_name,
            Correo=command.email,
            Clave=command.password,
            Telefono=command.phone,
            Activo=True,
            FechaHoraCreacion=datetime.datetime.now(),
            UsuarioCreacion='Dev'
        )
        self.mock_repository.save.return_value = mock_user
        
        result = self.use_case.execute(command)
        
        # validar q el resultado sea el usuario mockeado
        self.assertEqual(result, mock_user)

if __name__ == "__main__":
    unittest.main()