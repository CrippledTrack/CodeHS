--Made for Intro to SQL on CodeHS
Select Course.name AS "Course" , count(*) AS "Enrollment"
From Course join Enrollment
Where Course.id = Enrollment.course
Group by Course.id
Order by Enrollment desc, course.name;
