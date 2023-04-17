-- create table producers
-- insert couple of rows into producers
-- connect the apartment to producers
-- inner join producers with apartment 

-- create table producers (
-- id serial primary key,
-- first_name varchar(10),
-- last_name varchar(10)
-- );

-- insert into producers (first_name, last_name)
-- values
-- ('Kevin', 'Feige'),
-- ('Spike', 'Lee'),
-- ('Nina', 'Jacobson');

-- create table apartment (id serial primary key, location varchar(20));
-- insert into apartment (location)
-- values
-- ('Tel HaShomer'),
-- ('Tel Aviv'),
-- ('Tel Mond');

-- alter table producers 
-- add column Oscars smallint;

-- insert into producers (Oscars)
-- values 
-- (11),
-- (17),
-- (9);

-- select distinct first_name, last_name, location from
-- producers as p
-- join apartment as a
-- on p.id = a.resident_id

-- alter table apartment add constraint fk_producers
-- foreign key (producer_id) reference producers(id);

-- 				inner Join (just connects the valuse thaa are in between)

-- select first_name, last_name, location from 
-- apartment
-- join producers
-- on apartment.producers_id = producers.id

-- many to many relaitonship
-- one actor in multiple movies, one movie with multiple actors
-- actors -> actors.movies <- movies

-- create table movies (
-- id serial primary key,
-- title varchar(50)
-- );

-- create table actors_movies (
-- actor_id int references actors(id),
-- movie_id int references movies(id)
-- );

create table actors

-- insert into actors_movies (actor_id, movie_id)
-- values
-- (select id from actors where first_name = 'Tina')






















