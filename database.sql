CREATE TABLE IF NOT EXISTS users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_proxy VARCHAR (55),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_ip VARCHAR (55)
);

CREATE TABLE IF NOT EXISTS users_data (
    email VARCHAR (100) UNIQUE NOT NULL,
    password VARCHAR (50),
    user_ip VARCHAR (55)
);

CREATE TABLE IF NOT EXISTS proxy_data (
    proxy_id INT,
    proxy VARCHAR (55),
    result VARCHAR (25)
);
