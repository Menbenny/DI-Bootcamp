-- create table apartment (
-- id serial primary key,
-- location varchar(50),
-- actor_id int references actors (id)
-- );

-- insert into apartment (location, actor_id)
-- values
-- ('Tel Aviv', (select id from actors where first_name = 'Steve'));

select first_name, last_name, location 
from actors
join apartment 
-- for inner joint 
on actors, id = apartment.actor_id;   