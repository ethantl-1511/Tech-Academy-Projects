CREATE DATABASE db_movies
GO

CREATE TABLE actors (
	actorID INT PRIMARY KEY NOT NULL IDENTITY (1,1), -- Primary key
	first_name varchar(50), -- 'NOT NULL' isn't included in case name is unknown
	last_name varchar(50), -- 'NOT NULL' isn't included in case name is unknown
	movie_name varchar(50),
);

INSERT INTO actors
	(first_name, last_name, movie_name)
	VALUES
	('Mark', 'Hamill', 'Star Wars'),
	('Chris', 'Pratt', 'Gaurdians of the Galaxy'),
	('Harrison', 'Ford','Indiana Jones: Raiders of the Lost Ark'),
	('Kristen', 'Stewart','Twilight'),
	('Ronald', 'Reagan', '')
;

CREATE TABLE directors (
	directorID INT PRIMARY KEY NOT NULL IDENTITY (1,1), -- Primary key
	fname varchar(50),
	lname varchar(50),
	mname varchar(50),
	movieID INT FOREIGN KEY REFERENCES actors(actorID)
);


INSERT INTO directors
	(fname, lname, mname, movieID)
	VALUES
	('George', 'Lucus', 'Star Wars', '1'),
	('James', 'Gunn', 'Gaurdians of the Galaxy', '2'),
	('Steven', 'Spielberg','Indiana Jones: Raiders of the Lost Ark', '3'),
	('Catherine', 'Hardwicke','Twilight', '4'),
	('Francis', 'Coppola', 'The  Godfather', '5')
;

SELECT 
	first_name + ' ' + last_name AS "Actor Last Name",
	fname + ' ' + lname AS "Director Last Name"
FROM actors
	INNER JOIN directors ON actorID = movieID
WHERE mname = 'Star Wars';
