--Made for Intro to SQL on CodeHS
Select last_name, first_name
FROM Person Join course JOIN Enrollment
Where Person.id = Enrollment.person AND course.id = enrollment.course AND course.id = 1 AND Person.house <> 4
Order by last_name;
