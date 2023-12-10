--Made for Intro to SQL on CodeHS
Select Course.name AS "name", Person.first_name, Person.last_name, House.name as "house"
FROM Person Join Course Join House
WHERE Person.id = Course.professor AND House.id = Person.house
ORDER by Course.name;
