-- Say my Name
-- List all records of the table with a name

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY (score) DESC;
