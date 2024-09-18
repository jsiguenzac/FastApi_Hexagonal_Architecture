-- Seteo de codificación
SET client_encoding = 'UTF8';

CREATE TABLE public.tb_users (
    "idUsuario" BIGSERIAL PRIMARY KEY,
    "Nombre" character varying(50) NOT NULL,
    "Apellidos" character varying(80) NOT NULL,
    "Correo" character varying(100) NOT NULL,
    "Clave" character varying(300) NOT NULL,
    "Telefono" character varying(10),
    "Activo" boolean NOT NULL,
    "FechaHoraCreacion" TIMESTAMP,
    "UsuarioCreacion" character varying(50),
    "FechaHoraModificacion" TIMESTAMP,
    "UsuarioModificacion" character varying(50)
);

select * from tb_users