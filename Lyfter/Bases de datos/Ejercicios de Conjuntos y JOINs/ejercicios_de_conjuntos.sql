CREATE TABLE books (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255)
);

CREATE TABLE authors (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE costumers (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE rents (
    id INT PRIMARY KEY,
    book_id INT NOT NULL,
    costumer_id INT NOT NULL,
    state VARCHAR(50) NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (costumer_id) REFERENCES costumers(id)
);

INSERT INTO books (id, name, author) VALUES
(1, 'Don Quixote', '1'),
(2, 'La divina comedia', '2'),
(3, 'Vagabond 1-3', '3'),
(4, 'Dragon Ball 1-3', '4'),
(5, 'The book of the 5 rings', '5'); 

INSERT INTO authors (id, name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT INTO costumers (id, name, email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane.doe@email.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO rents (id, book_id, costumer_id, state) VALUES
(1, 1, 1, 'returned'),
(2, 2, 1, 'returned'),
(3, 3, 2, 'on time'),
(4, 4, 3, 'on time'),
(5, 5, 3, 'overdue');

SELECT * 
FROM books
LEFT JOIN authors
ON books.author = authors.id;

SELECT *
FROM books
LEFT JOIN authors ON books.author = authors.id
WHERE authors.name is NULL;

SELECT * 
FROM authors
LEFT JOIN books
ON authors.id = books.author
WHERE books.name is NULL;       

SELECT *
FROM books
INNER JOIN rents 
ON books.id = rents.book_id;

SELECT *
FROM books
LEFT JOIN rents 
ON books.id = rents.book_id
WHERE rents.state IS NULL;

SELECT *
FROM costumers
LEFT JOIN rents
ON costumers.id = rents.costumer_id
WHERE rents.state IS NULL;

SELECT *
FROM books
INNER JOIN rents
ON books.id = rents.book_id
WHERE rents.state = 'overdue';