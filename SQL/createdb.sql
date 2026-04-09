-- Create a database for your company named XYZ.
-- Step 1: Create a table inside this DB to store employee info (id, name, and salary).
-- Step 2: Add the following information in the DB:
-- 1, "adam", 25000
-- 2, "bob", 30000
-- 3, "casey", 40000
-- Step 3: Select & view all your table data.

create database XYZ;
use XYZ;
create table employees (
    id int,
    name varchar(50),
    salary int
);

insert into employees (id, name, salary)
values 
(1, 'adam', 25000),
(2, 'bob', 30000)
(3, 'casey', 40000);