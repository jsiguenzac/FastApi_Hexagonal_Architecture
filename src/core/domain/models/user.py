from src.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class User(Base):
    __tablename__ = 'tb_users'

    idUsuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Nombre = Column(String(50), nullable=False)
    Apellidos = Column(String(80), nullable=False)
    Correo = Column(String(100), nullable=False)
    Clave = Column(String(300), nullable=False)
    Telefono = Column(String(10), nullable=True)
    Activo = Column(Boolean, default=True)    
    FechaHoraCreacion = Column(DateTime, nullable=True)
    UsuarioCreacion = Column(String(50), nullable=True)
    FechaHoraModificacion = Column(DateTime, nullable=True)
    UsuarioModificacion = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"<Usuarios(idUsuario={self.idUsuario}, Nombre={self.Nombre}, Activo={self.Activo})>"