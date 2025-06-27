-- Group the result data by a given column
SELECT `score`, COUNT(`id`) AS number FROM second_table GROUP BY score;