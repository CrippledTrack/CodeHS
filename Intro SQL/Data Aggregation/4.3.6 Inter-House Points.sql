--Made for Intro to SQL on CodeHS
SELECT Professor.first_name, Professor.last_name, Sum(points) AS "points"
FROM HousePoint
JOIN Person AS Professor
JOIN Person AS Student
JOIN House AS ProfHouse
JOIN House AS StudHouse

WHERE HousePoint.giver = Professor.id
AND HousePoint.receiver = Student.id
AND ProfHouse.id = Professor.house
AND StudHouse.id = Student.house
AND Professor.house <> Student.house
GROUP BY Professor.id
ORDER BY Sum(points) DESC;
