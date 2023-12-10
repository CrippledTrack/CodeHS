--Made for Intro to SQL on CodeHS
SELECT House.name AS "House", Sum(points)AS "Points"
FROM House JOIN HousePoint JOIN Person
WHERE House.id = Person.house
AND Person.id = HousePoint.receiver
GROUP BY House.name
ORDER BY Sum(points) DESC;
