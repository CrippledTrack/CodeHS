--Made for Intro to SQL on CodeHS
Select House.name AS "House" , count(Person.last_name) As "Professors"
From House JOIN Person JOIN Course
Where Person.house = house.id
AND Person.id = Course.professor
Group by House.name
Order by House.name;
