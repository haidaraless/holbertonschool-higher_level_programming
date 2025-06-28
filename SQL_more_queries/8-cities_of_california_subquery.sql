-- Perform subquery to get cities of a given state

SELECT `id`, `name` FROM cities WHERE state_id = (SELECT `id` FROM states WHERE `name` = "California");