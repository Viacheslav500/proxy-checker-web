CREATE DATABASE IF NOT EXISTS proxy_checker_db;
USE proxy_checker_db;

CREATE TABLE IF NOT EXISTS users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_proxy VARCHAR (55),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_ip VARCHAR (55)
);

CREATE TABLE IF NOT EXISTS users_data (
    users_id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR (100) UNIQUE NOT NULL,
    password_hash VARCHAR (255),
    user_ip VARCHAR (45)
);

CREATE TABLE IF NOT EXISTS proxy_data (
    proxy_id INT AUTO_INCREMENT PRIMARY KEY,
    proxy VARCHAR (55),
    result VARCHAR (25),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
