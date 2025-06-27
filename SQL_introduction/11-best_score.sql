-- Get all records that matches a condition sorted by bigger score
SELECT `score`, `name` FROM second_table WHERE score >= 10 ORDER BY score DESC;