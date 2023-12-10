--Made for Intro to SQL on CodeHS
SELECT Person.first_name AS "Name", sum(HousePoint.points) as "Points"
FROM Person JOIN HousePoint
Where Person.last_name = "Weasley"
AND Person.id = HousePoint.receiver
GROUP by HousePoint.receiver
ORDER BY HousePoint.points desc;
