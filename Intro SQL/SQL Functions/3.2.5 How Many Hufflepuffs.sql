--Made for Intro to SQL on CodeHS
SELECT Course.name AS "Course" , count(*) AS "Enrollment"
FROM Course JOIN Enrollment JOIN Person
WHERE Course.id = Enrollment.course
AND Person.id = Enrollment.person
AND Person.house = 2
GROUP BY Course.id
ORDER BY Enrollment DESC;
