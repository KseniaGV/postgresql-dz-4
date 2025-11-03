--задание 2
select name, duration from track
order by duration desc
limit 1;

select name, duration from track
where duration >= '00:03:30';

select name, year_of_manufacture from collection
where year_of_manufacture between '2018-01-01' and '2021-01-01';

select name from executorr 
where name not like '% %';

select name from track
where name like '%my%' or name like '%мой%';

--задание 3
select id_genre, count(*) from eg
group by id_genre;

SELECT count(*) FROM album a
JOIN track ON a.id = track.id_album
WHERE year_of_manufacture between '2019-01-01' and '2021-01-01';

SELECT a.name, avg(duration) FROM album a
JOIN track ON a.id = track.id_album
group by a.name;

SELECT e.name FROM ea
JOIN executorr as e ON e.id = ea.id_executor
join album as a on a.id = ea.id_album
where year_of_manufacture not between '2019-01-01' and '2021-01-01'
group by e.name;

SELECT c.name FROM ct
join collection as c on c.id = ct.id_collection
join track as t ON ct.id_track = t.id
join album as a on a.id = t.id_album
join ea  on ea.id_album = a.id
JOIN executorr as e ON e.id = ea.id_executor
where e.name = 'Тейлор свифт'
group by c.name;









