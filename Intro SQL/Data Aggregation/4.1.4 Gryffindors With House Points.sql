--Made for Intro to SQL on CodeHS
SELECT Person.first_name, Person.last_name, HousePoint.points
FROM Person JOIN HousePoint
Where HousePoint.receiver = Person.id
AND Person.house = 1
ORDER by HousePoint.points DESC,Person.last_name desc,Person.first_name desc;
