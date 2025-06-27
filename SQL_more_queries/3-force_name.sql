-- Creates a table and it fields that doesn't accepts null value

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);