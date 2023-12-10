--Made for Intro to SQL on CodeHS
SELECT
    Person.first_name,
    Person.last_name,
    COALESCE(SUM(HousePoint.points), 0) AS Points
FROM
    Person
JOIN
    HousePoint ON Person.id = HousePoint.giver
WHERE
    HousePoint.points < 0
GROUP BY
    Person.id, Person.first_name, Person.last_name
ORDER BY
    Points ASC, Person.last_name, Person.first_name
LIMIT 4;
