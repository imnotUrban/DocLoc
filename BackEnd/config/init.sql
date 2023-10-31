-- Crear un usuario con privilegios de administrador
CREATE USER 'admin'@'0.0.0.0' IDENTIFIED BY '1234';

-- Asignar privilegios de administrador al usuario
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'0.0.0.0';
FLUSH PRIVILEGES;

-- Crear una base de datos
CREATE DATABASE IF NOT EXISTS storedb CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE storedb;
ALTER TABLE documents MODIFY text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
