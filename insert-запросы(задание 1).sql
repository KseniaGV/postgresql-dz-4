--задание 1
INSERT INTO executorr(name) 
VALUES('Тейлор свифт'), ('Джастин Бибер'), ('Кино'), ('Баста');

insert into genre(name)
values ('Поп'), ('Рок'), ('Рэп');

insert into album(name, year_of_manufacture)
values ('Reputation', '2017-11-10'), ('Swag', '2025-07-11'), ('Баста 4', '2020-11-20');

insert into track(name, duration, id_album)
values ('king of my heart', '00:03:34', 1), ('delicate', '00:03:55', 1), ('way it is', '00:03:15', 2), ('405', '00:03:33', 2), ('мама', '00:04:56', 3), ('вселенная', '00:03:32', 3);

insert into collection(name, year_of_manufacture)
values('The Best Of', '2017-02-16'), ('Mixtape', '2019-05-30'), ('Песни о любви', '2020-09-03'), ('Песни для зимнего вечера', '2015-12-01');

insert into eg(id_executor, id_genre)
values(1, 1), (2, 1), (3, 2), (4, 3);

insert into ea(id_executor, id_album)
values(1, 1), (2, 2), (4, 3);

insert into ct(id_collection, id_track)
values(1, 5), (2, 4), (3, 1), (4, 2), (2, 3), (3, 6);