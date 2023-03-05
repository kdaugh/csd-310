USE whatabook;

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;


-- create the user table 
CREATE TABLE user (
    user_id     INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    Last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
); 

-- create the book table
CREATE TABLE book (
    book_id     INT             NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

-- create the wishlist table and set the foreign key
CREATE TABLE wishlist (
    wishlist_id INT             NOT NULL        AUTO_INCREMENT,
    user_id     INT             NOT NULL,
    book_id     INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY(user_id) 
        REFERENCES user(user_id),
    CONSTRAINT fk_user
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

-- create the store table
CREATE TABLE store (
    store_id    INT             NOT NULL        AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    hours       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(store_id)
);


-- insert store records
INSERT INTO store(locale)
    VALUES('12345 Whatabook Rd, Somewhere, NE 65432');

-- insert book records
INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 1', 'Details on book 1', 'Author 1');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 2', 'Details on book 2', 'Author 2');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 3', 'Details on book 3', 'Author 3');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 4', 'Details on book 4', 'Author 4');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 5', 'Details on book 5', 'Author 5');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 6', 'Details on book 6', 'Author 6');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 7', 'Details on book 7', 'Author 7');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 8', 'Details on book 8', 'Author 8');

INSERT INTO book(book_name, details, author) 
    VALUES('Book Name 9', 'Details on book 9', 'Author 9');

-- insert user records 
INSERT INTO user(first_name, last_name) 
    VALUES('Don', 'Donaldson');

INSERT INTO user(first_name, last_name)
    VALUES('Bob', 'Bobertson');

INSERT INTO user(first_name, last_name)
    VALUES('Phil', 'Philips');

-- insert wishlist records 
INSERT INTO wishlist(user_id, book_id) VALUES(1, 1);

INSERT INTO wishlist(user_id, book_id) VALUES(2, 7);

INSERT INTO wishlist(user_id, book_id) VALUES(3, 5);