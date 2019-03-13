CREATE TABLE books (
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER NOT NULL
);
INSERT INTO books (isbn, title, author, year) VALUES (isbn, title, author, year);

CREATE TABLE users (
    username VARCHAR NULL UNIQUE,
    password VARCHAR NULL
);