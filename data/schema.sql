CREATE DATABASE kuorra_access;

USE kuorra_access;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    api_access integer NOT NULL DEFAULT 0,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE pages_urls( 
    id_page_url integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_np varchar(50) NOT NULL,
    get_url integer NOT NULL,
    post_url integer NOT NULL,
    controller VARCHAR(50) NOT NULL,
    c_view VARCHAR(50) NOT NULL,
    url_full VARCHAR(300) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos( 
    id_producto integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    producto varchar(400) NOT NULL,
    existencias integer NOT NULL,
    precio float NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);

INSERT INTO pages_urls (user_np, get_url, post_url, controller, c_view, url_full) VALUES ("0", 1 , 1 , "productos", "index", "/productos");
INSERT INTO pages_urls (user_np, get_url, post_url, controller, c_view, url_full) VALUES ("1", 1 , 1 , "productos", "index", "/productos");

INSERT INTO productos (producto, existencias, precio) VALUES ("smartwatch",10,2000.00);

SELECT * FROM users;
SELECT * FROM sessions;
SELECT * FROM pages_urls;

SELECT * FROM productos;

/*
CREATE USER 'kuorra00'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON kuorra_access.* TO 'kuorra00'@'localhost';
FLUSH PRIVILEGES;
*/