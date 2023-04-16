-- create table students (
-- 	id serial primary key,
-- 	last_name varchar(10),
-- 	first_name varchar(10),
-- 	birth_date date
-- )
-- select * from students;
-- insert into students (last_name, first_name, birth_date)
-- values
-- ('Benichou', 'Marc', make_date(1998, 02, 11)) created
-- ('Cohen', 'Yoan', make_date(2010, 03, 12)) created
-- ('Benichou', 'Lea', '1987-07-27')
-- ('Dux', 'Amelia', make_date (1996, 07, 04)) created
-- ('Grez', 'David', '2003-06-14') 
-- ('Simpson', 'Omer', make_date(1980, 03, 10)) created

-- insert into students()

-- 1.
-- select * from students

-- 2.
-- select first_name, last_name from students 

-- 3.
-- select * from students where id = 2
-- select * from students where last_name = 'Benichou' OR first_name = 'Marc'
-- select first_name from students where first_name like '%a%'
-- select first_name from students where first_name like 'A%'
-- select first_name from students where first_name ilike '%a'     (ilike kills case sensitivity)
-- select first_name from students where first_name ilike '%a_'
-- select * from students where id = 1 or id = 3

-- 4.
-- select * from students where birth_date >= '2000-01-01'