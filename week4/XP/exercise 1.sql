  				-- EXERCISE 1 -- 

-- 1.
-- create table items (
-- 	id serial primary key,
-- 	descrption varchar(3),
-- 	price int
-- );

-- 2.
-- create table customers (
-- id serial primary key,
-- 	name varchar(5)
-- );

-- alter table customers
-- add column last_name varchar(5);
	
-- alter table items
-- alter column descrption TYPE varchar(12)

-- alter table customers 
-- alter column name TYPE varchar(12)
-- alter column last_name TYPE varchar(12)

-- insert into items (descrption, price)
-- values
-- 	('Small_desk', 100),
-- 	('Large_desk', 300),
-- 	('Fan', 80);


-- insert into customers (name, last_name)
-- values
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson');

-- 3.
-- select * 
-- from items 
-- join customers on items.* = customers.*

-- select price from items where price > 81

-- select price from items where price = 300 or price < 300

-- select last_name from customers where last_name = 'Smith'

-- select last_name from customers where last_name = 'Jones'

select name from customers where last_name != 'Scott'




