--Made for Intro to SQL on CodeHS
SELECT Person.First_name, person.Last_name, count(Enrollment.course) AS courses
FROM Person JOIN Course JOIN Enrollment
Where person.id = enrollment.person
AND course.id = enrollment.course
group by Enrollment.person
order by courses desc, last_name
limit 5;
