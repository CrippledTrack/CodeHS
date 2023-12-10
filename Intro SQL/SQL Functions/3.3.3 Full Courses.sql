--Made for Intro to SQL on CodeHS
SELECT Course.name AS Course, Person.Last_name AS "Professor Last Name", count(Enrollment.course) as Enrollment
From House JOIN Person JOIN Course JOIN Enrollment
WHERE Person.id = Course.professor
AND House.id = Person.house
AND Enrollment.course = Course.id
Group by course.id
Order by Enrollment desc
-- This Code will only be correct if there are only 2 classes with 18 students
LIMIT 2;
