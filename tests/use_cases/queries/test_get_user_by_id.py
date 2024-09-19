import unittest
from unittest.mock import Mock
from src.core.use_cases.queries.get_user_by_id import GetUserByIdUseCase
from src.core.domain.models.user import User

class TestGetUserByIdUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock()
        self.use_case = GetUserByIdUseCase(self.mock_repository)
    
    def test_execute(self):
        # Simular un usuario de prueba
        mock_user = User(
            idUsuario=1,
            Nombre="Joel",
            Apellidos="Sigüenza",
            Correo="siguenzajoel10@gmail.com",
            Clave="76411904",
            Telefono="921018664",
            Activo=True,
            FechaHoraCreacion="2024-09-18",
            UsuarioCreacion="Dev"
        )
        self.mock_repository.get_by_id.return_value = mock_user
        user_id = 1
        result = self.use_case.execute(user_id)

        # validar si el metodo fue llamado con el user_id correcto
        self.mock_repository.get_by_id.assert_called_once_with(user_id)

        # validar q el resultado sea el usuario esperado
        self.assertEqual(result, mock_user)

if __name__ == "__main__":
    unittest.main()