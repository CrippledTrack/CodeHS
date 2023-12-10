--Made for Intro to SQL on CodeHS
Select course.name
FROM Person Join course JOIN Enrollment
Where Person.id = Enrollment.person AND course.id = enrollment.course AND Person.id=15
Order by course.name;
