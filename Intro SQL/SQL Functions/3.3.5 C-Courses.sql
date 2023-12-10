--Made for Intro to SQL on CodeHS
Select Course.name as "Course"
From Course JOIN Enrollment
Where course.id = Enrollment.course
AND Course.name LIKE "C%"
group by Course.name
Having count(*)>15;
