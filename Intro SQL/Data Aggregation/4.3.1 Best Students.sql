--Made for Intro to SQL on CodeHS
SELECT
    Person.first_name,
    Person.last_name,
    COALESCE(SUM(HousePoint.points), 0) AS Points
FROM
    Person
LEFT JOIN
    HousePoint ON Person.id = HousePoint.receiver
GROUP BY
    Person.id, Person.first_name, Person.last_name
ORDER BY
    Points DESC
LIMIT 2;
