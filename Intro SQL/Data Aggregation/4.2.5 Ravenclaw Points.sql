--Made for Intro to SQL on CodeHS
SELECT SUM(hp.points) AS "Points"
FROM HousePoint JOIN Person
WHERE Person.id = HousePoint.receiver
AND Person.house=3;
