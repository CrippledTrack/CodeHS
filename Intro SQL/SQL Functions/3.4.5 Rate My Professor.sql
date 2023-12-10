--Made for Intro to SQL on CodeHS
SELECT Person.first_name, person.last_name
FROM Course
JOIN Person on Course.professor = Person.id 
JOIN enrollment ON Course.id = Enrollment.course
GROUP by course.id, Person.id
ORDER BY COUNT(Enrollment.course) 
LIMIT 1;
