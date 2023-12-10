--Made for Intro to SQL on CodeHS
SELECT house.name AS "House"
FROM House JOIN Person JOIN HousePoint
WHERE house.id = Person.house
Order by HousePoint.points
limit 1;
