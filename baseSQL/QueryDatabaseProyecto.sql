CREATE DATABASE PROYECTO;

USE PROYECTO;
GO

CREATE TABLE usuarios(
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE tareas(
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion VARCHAR(100),
    asignadoA INT NOT NULL,
    FOREIGN KEY (asignadoA) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE notificaciones(
    idTarea INT NOT NULL,
    mensaje VARCHAR(500) NOT NULL,
    asignado INT NOT NULL,
    fecha DATETIME DEFAULT GETDATE(),
    PRIMARY KEY (idTarea, asignado),
    FOREIGN KEY (idTarea) REFERENCES tareas(id) ON DELETE CASCADE,
    FOREIGN KEY (asignado) REFERENCES usuarios(id) ON DELETE NO ACTION
);

SELECT * FROM notificaciones;
SELECT * FROM usuarios;
SELECT * FROM tareas;
