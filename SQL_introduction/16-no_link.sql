-- List all records of the table excepts null values
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY score DESC;