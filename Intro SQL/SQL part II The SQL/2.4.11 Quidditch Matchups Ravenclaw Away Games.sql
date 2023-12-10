--Made for Intro to SQL on CodeHS
SELECT Home.name AS Home, Away.name AS Away
FROM House AS Home, House AS Away
WHERE Away.name = "Ravenclaw" and Home.name <> Away.name;
