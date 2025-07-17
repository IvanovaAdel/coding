CREATE TABLE autors (
	id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
  );

insert into autors (first_name, last_name) values ("Федор", "Достоевский");
insert into autors (first_name, last_name) values ("Александ", "Пушкин");
insert into autors (first_name, last_name) values ("Михаил", "Булгаков");


  SELECT * FROM autors;
  
  CREATE TABLE publishers(
  	id INT NOT NULL AUTO_INCREMENT,
  	name VARCHAR(100) NOT NULL,
  	PRIMARY KEY (id));
insert into publishers (name) values ("2");
insert into publishers (name) values ("1");

SELECT * FROM publishers;

CREATE TABLE books(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author_id INT NOT NULL,
    publisher_id INT NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES autors(id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);
insert into books (title, author_id, publisher_id, year) values ("книга 1", "3", "1", "1990");
insert into books (title, author_id, publisher_id, year) values ("книга 2", "2", "1", "1950");
insert into books (title, author_id, publisher_id, year) values ("книга 3", "1", "2", "1350");
insert into books (title, author_id, publisher_id, year) values ("книга 4", "3", "2", "1890");

SELECT title FROM books where year = '1990';
update books set year = '1323' where title = 'книга 1';

SELECT id FROM autors;
SELECT * FROM books;

SELECT id FROM publishers;
