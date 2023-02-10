-- Challenge 1 --
SELECT DISTINCT FirstName
FROM Person.Person

-- Challenge 2 --
SELECT TOP 1 PERCENT FirstName
FROM Person.Person

-- Challenge 3 --
SELECT Max(BusinessEntityID)
FROM Person.Person

-- Challenge 4 & 5 --
SELECT *
FROM Person.Person
WHERE LastName LIKE 'La%';

-- Challenge 6 --

SELECT LastName
FROM Person.Person
WHERE LastName BETWEEN 'Ba%' AND 'Bz%';
