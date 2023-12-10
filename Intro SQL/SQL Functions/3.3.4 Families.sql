--Made for Intro to SQL on CodeHS
SELECT Person.Last_name AS "Family", count(person.last_name) AS "Count"
From Person
Group by Last_name
Having count(*)>1
Order by "COUNT" DESC;
