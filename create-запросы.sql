create table IF NOT exists genre (
id serial primary key,
name varchar(60) not null
);

create table IF NOT exists executorr (
id serial primary key,
name varchar(60) not null
);

create table IF NOT exists album (
id serial primary key,
name varchar(60) not null,
year_of_manufacture date not null
);

create table IF NOT exists collection (
id serial primary key,
name varchar(60) not null,
year_of_manufacture date not null
);

create table IF NOT exists track (
id serial primary key,
name varchar(60) not null,
duration time not null,
id_album integer not null,
foreign key(id_album) references album(id)
);

create table IF NOT exists eg (
id serial primary key,
id_executor integer,
id_genre integer,
foreign key (id_genre) references genre(id),
foreign key (id_executor) references executorr(id)
);

create table IF NOT exists ea (
id serial primary key,
id_executor integer,
id_album integer,
foreign key (id_album) references album(id),
foreign key (id_executor) references executorr(id)
);

create table IF NOT exists ct (
id serial primary key,
id_track integer,
id_collection integer,
foreign key (id_track) references track(id),
foreign key (id_collection) references collection(id)
);

