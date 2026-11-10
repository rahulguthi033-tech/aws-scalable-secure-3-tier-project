CREATE DATABASE IF NOT EXISTS rahul_app;

USE rahul_app;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT IGNORE INTO users (name, email)
VALUES
('Rahul', 'rahul@example.com'),
('DevOps Student', 'student@example.com');
