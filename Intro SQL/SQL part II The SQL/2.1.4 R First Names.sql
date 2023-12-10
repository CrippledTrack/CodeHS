--Made for Intro to SQL on CodeHS
SELECT first_name,last_name
FROM Person
Where house=4 
AND first_name LIKE "R%" 
OR house=1
AND first_name LIKE "R%";
