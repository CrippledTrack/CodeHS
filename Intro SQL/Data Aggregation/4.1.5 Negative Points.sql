--Made for Intro to SQL on CodeHS
SELECT Person.first_name, Person.last_name, HousePoint.points
FROM Person JOIN HousePoint
WHERE HousePoint.receiver = Person.id
AND HousePoint.points < 0
ORDER BY HousePoint.points, Person.last_name, Person.first_name;
