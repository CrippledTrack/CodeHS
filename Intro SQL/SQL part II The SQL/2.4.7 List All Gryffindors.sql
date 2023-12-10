--Made for Intro to SQL on CodeHS
SELECT Person.first_name, Person.last_name, House.name as house
FROM Person JOIN House
WHERE Person.house = House.id AND house.id=1
Order by first_name;
