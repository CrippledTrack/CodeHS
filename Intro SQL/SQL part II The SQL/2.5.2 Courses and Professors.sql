--Made for Intro to SQl on CodeHS
Select Course.name AS name, Person.first_name,Person.last_name
FROM Person Join Course
WHERE Person.id = Course.professor
ORDER by Course.name;
