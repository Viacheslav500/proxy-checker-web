CREATE TABLE IF NOT EXISTS users(
    user_id PRIMARY KEY AUTO_INCREMENT,
    user_proxy VARCHAR (55),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_ip VARCHAR (55)
);

CREATE TABLE IF NOT EXISTS users_data (
    email VARCHAR (100) UNIQUE,
    password VARCHAR (50) UNIQUE,
    user_ip VARCHAR (55)
);

CREATE TABLE IF NOT EXISTS proxy_data (
    proxy_id INTEGER,
    proxy VARCHAR (55),
    result VARCHAR (25)
);
