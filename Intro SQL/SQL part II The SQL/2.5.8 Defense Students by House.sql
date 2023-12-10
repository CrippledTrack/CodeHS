--Made for Intro to SQL on CodeHS
Select last_name, first_name, house.name AS house
FROM Person Join course JOIN Enrollment JOIN House
Where Person.id = Enrollment.person AND course.id = enrollment.course AND course.id = 5 AND House.id = Person.house
Order by House.id, Person.last_name, Person.first_name;
