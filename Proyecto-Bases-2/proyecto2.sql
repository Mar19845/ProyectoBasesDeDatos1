create table usuario(
usuario varchar primary key not null,
contrasenia varchar not null,
logins int not null,
suscripcion bool,
administrador bool,
id_tipo_admin int,
activado bool,
foreign key (id_tipo_admin) references tipo_admins(id_tipo_admin) on delete cascade
);

create table tipo_admins(
id_tipo_admin serial primary key not null,
tareas_puede_realizar varchar
);

create table canciones(
id serial primary key not null,
cancion varchar not null,
link varchar not null,
artista varchar not null,
activa bool
);

create table albumes(
nombre varchar primary key not null,
genero varchar not null,
creador varchar not null,
fecha_salida date not null,
activo bool
);

create table album_cancion(
id_album_cancion serial primary key not null,
id_cancion int not null,
id_album varchar not null,
foreign key (id_cancion) references canciones(id) on delete cascade,
foreign key (id_album) references albumes(nombre) on delete cascade
);

create table artistas(
nombre varchar primary key not null,
usuario varchar not null,
foreign key (usuario) references usuario(usuario) on delete cascade
);

create table playlist(
id serial primary key not null,
nombre varchar not null,
nombre_usuario varchar not null,
foreign key (nombre_usuario) references usuario(usuario) on delete cascade
);

create table playlist_cancion(
id_playlist_cancion serial primary key not null,
id_cancion int not null,
id_playlist int not null,
foreign key (id_cancion) references canciones(id) on delete cascade,
foreign key (id_playlist) references playlist(id) on delete cascade
);

create table managers(
nombre varchar primary key not null,
artista_representa varchar not null,
foreign key (artista_representa) references artistas(nombre) on delete cascade
);

create table reproducciones(
id_repro serial primary key not null,
id_cancion int not null,
fecha date not null,
foreign key (id_cancion) references canciones(id) on delete cascade
);

drop table usuario;
drop table tipo_admins;
drop table canciones cascade;
drop table albumes cascade;
drop table album_cancion;
drop table artistas;
drop table playlist;
drop table playlist_cancion;
drop table managers;
drop table reproducciones;

select * from usuario;
select * from tipo_admins;
select * from canciones;
select * from albumes;
select * from album_cancion;
select * from artistas;
select * from playlist;
select * from playlist_cancion;
select * from managers;
select * from reproducciones;

insert into tipo_admins
values (1, 'Modificar la información de cualquier track y álbum del catálogo, Eliminar suscripciones de usuarios'),
(2, 'Desactivar tracks y álbumes, Desactivar usuarios sin suscripción para que ya no puedan acceder a la plataforma, Desactivar usuarios registrados como artistas'),
(3, 'Asociar un usuario existente a un perfiles de monitoreo, Generar los reportes ofrecidos por la plataforma, Consulta de bitácora de operaciones');

insert into usuario
values ('user1', 'abc', 5, false, false, 1, true),
('user2', '123', 10, true, true, 2, true),
('user3', 'abcd', 15, false, false, 3, true),
('user4', '1234', 20, true, true, 1, true),
('user5', 'abcde', 25, false, false, 2, true);

insert into canciones(cancion, link, artista, activa)
values ('Toosie Slide', 'https://www.youtube.com/watch?v=xWggTb45brM', 'Drake', true),
('Alone', 'https://www.youtube.com/watch?v=1-xGerv5FOk', 'Alan Walker', true),
('Azul', 'https://www.youtube.com/watch?v=bcaLBKH-Yfc', 'J Balvin', true),
('Back In Black', 'https://www.youtube.com/watch?v=pAgnJDJN4VA', 'AC/DC', true),
('Dura', 'https://www.youtube.com/watch?v=sGIm0-dQd8M', 'Daddy Yankee', true);

insert into albumes
values ('Toosie Slide', 'Rap', 'Drake', '2020-04-03', true),
('Alone', 'Electrónica', 'Alan Walker', '2016-12-02', true),
('Colores', 'Reggaeton', 'J Balvin', '2020-06-05', true),
('Back In Black', 'Rock', 'AC/DC', '1980-07-25', true),
('Dura', 'Reggaeton', 'Daddy Yankee', '2018-01-18', true);

insert into album_cancion(id_cancion, id_album)
values (1, 'Toosie Slide'),
(2, 'Alone'),
(3, 'Colores'),
(4, 'Back In Black'),
(5, 'Dura');

insert into artistas
values ('Drake', 'user1'),
('Alan Walker', 'user2'),
('J Balvin', 'user3'),
('AC/DC', 'user4'),
('Daddy Yankee', 'user5');

insert into playlist(nombre, nombre_usuario)
values ('playlist1', 'user1'),
('playlist2', 'user2'),
('playlist3', 'user3'),
('playlist4', 'user4'),
('playlist5', 'user5');

insert into playlist_cancion(id_cancion, id_playlist)
values (1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

insert into managers
values ('manager1', 'Drake'),
('manager2', 'Alan Walker'),
('manager3', 'J Balvin'),
('manager4', 'AC/DC'),
('manager5', 'Daddy Yankee');

insert into reproducciones(id_cancion, fecha)
values (1, '2021-01-02'),
(2, '2021-02-03'),
(3, '2021-03-04'),
(4, '2021-04-05'),
(5, '2021-05-01');

select cancion
from canciones
where cancion ilike '%TOO%';

select p.nombre
from playlist p
inner join playlist_cancion pc on p.id = pc.id_playlist
where pc.id_cancion = 1;

select p.nombre
from playlist p
inner join playlist_cancion pc on p.id = pc.id_playlist
where pc.id_cancion = 1
and p.nombre ilike '%PLAY%';

select usuario
from usuario
where suscripcion = true;

select nombre
from albumes
where genero = 'Reggaeton';

select nombre
from albumes
where creador = 'Drake';

select nombre
from artistas
where nombre ilike '%al%';

SELECT a.nombre from albumes a WHERE a.fecha_salida > (SELECT CAST(NOW() AS DATE) - 7);

SELECT al.creador, count(r)
FROM album_cancion ac
INNER JOIN canciones c on ac.id_cancion = c.id
INNER JOIN albumes al on ac.id_album = al.nombre
INNER JOIN reproducciones r on r.id_cancion = c.id
WHERE r.fecha > (SELECT CAST(NOW() AS DATE) - 90)
GROUP BY al.creador
ORDER BY count(r) desc;

SELECT ar.nombre, count(r)
FROM artistas ar
INNER JOIN albumes al on ar.nombre = al.creador
INNER JOIN canciones c on c.cancion = c.cancion
INNER JOIN reproducciones r on r.id_cancion = c.id
GROUP BY ar.nombre
ORDER BY count(r) desc;

SELECT usuario, logins FROM usuario ORDER BY logins DESC LIMIT 5;

create or replace function tarea1_1(id_i int, cancion_i varchar, link_i varchar, artista_i varchar)
returns canciones as $$
begin
	update canciones set cancion = cancion_i, link = link_i, artista = artista_i
	where id = id_i;
	return null;
end;
$$
language 'plpgsql';

select tarea1_1(1, 'Toosie Slide', 'https://www.youtube.com/watch?v=xWggTb45brM', 'Drake');
select * from canciones;

create or replace function tarea1_2(nombre_i varchar, genero_i varchar, creador_i varchar, fecha_salida_i date)
returns albumes as $$
begin
	update albumes set genero = genero_i, creador = creador_i, fecha_salida = fecha_salida_i
	where nombre = nombre_i;
	return null;
end;
$$
language 'plpgsql';

select tarea1_2('Toosie Slide', 'Rap', 'Drake', '2020-04-03');
select * from albumes;

create or replace function tarea2_1(id_i int, activa_i bool)
returns canciones as $$
begin
	update canciones set activa = activa_i
	where id = id_i;
	return null;
end;
$$
language 'plpgsql';

select tarea2_1(1, true);
select * from canciones;

create or replace function tarea2_2(nombre_i varchar, activo_i bool)
returns albumes as $$
begin
	update albumes set activo = activo_i
	where nombre = nombre_i;
	return null;
end;
$$
language 'plpgsql';

select tarea2_2('Toosie Slide', true);
select * from albumes;

create or replace function tarea3(usuario_i varchar, activado_i bool)
returns usuario as $$
begin
	update usuario set activado = activado_i
	where usuario = usuario_i
	and suscripcion = false;
	return null;
end;
$$
language 'plpgsql';

select tarea3('user2', false);
select * from usuario;

create or replace function tarea4(usuario_i varchar, suscripcion_i bool)
returns usuario as $$
begin
	update usuario set suscripcion = suscripcion_i
	where usuario = usuario_i;
	return null;
end;
$$
language 'plpgsql';

select tarea4('user1', false);
select * from usuario;

create or replace function tarea5(usuario_i varchar, activado_i bool)
returns usuario as $$
begin
	update usuario set activado = activado_i
	where usuario = usuario_i
	and usuario_i in (select usuario from artistas);
	return null;
end;
$$
language 'plpgsql';

select tarea5('user6', false);
select * from usuario;
insert into usuario values ('user6', '12345', 30, true, true, 2, true);

create or replace function tarea6(usuario_i varchar, perfil int)
returns usuario as $$
begin
	update usuario set id_tipo_admin = perfil
	where usuario = usuario_i;
	return null;
end;
$$
language 'plpgsql';

select tarea6('user6', 2);
select * from usuario;

select c.artista, (count(r))*(1/1000) as comision_en_dolares
from canciones c
inner join reproducciones r on r.id_cancion = c.id
inner join artistas a on c.artista = a.nombre
group by c.artista;

create or replace function repro_semana(fecha_i date, fecha_f date)
returns table(year_week text, repro_count int8) as $$
begin
	return query	SELECT t1.year_week week, t2.repro_count 
					FROM (
						SELECT week, To_char(week, 'IYYY-IW') year_week 
						FROM generate_series(fecha_i::DATE, fecha_f::DATE, '1 week'::interval) AS week
					) t1 
						 LEFT OUTER JOIN (
						 	SELECT To_char(r.fecha, 'IYYY-IW') year_week, COUNT(r) repro_count 
	  					    from reproducciones r
						    GROUP BY year_week
						 ) t2 
							  ON t1.year_week = t2.year_week;
end;
$$
language 'plpgsql';

select repro_semana('2021-01-01', '2021-05-02');
select * from reproducciones;

create or replace function artistas_repro(fecha_i date, fecha_f date, cantidad_artistas int)
returns table(artista_f varchar, repro_count int8) as $$
begin
	return query	select ar.nombre, count(r)
					from canciones c
						inner join reproducciones r	on r.id_cancion = c.id
						inner join artistas ar on ar.nombre = c.artista
					where r.fecha >= fecha_i
					and r.fecha <= fecha_f
					group by ar.nombre
					order by count(r)
					limit cantidad_artistas;
end;
$$
language 'plpgsql';

select artistas_repro('2021-01-01', '2021-05-02', 5);

create or replace function repro_genero(fecha_i date, fecha_f date)
returns table(genero_f varchar, repro_count int8) as $$
begin
	return query	select al.genero, count(r)
					from canciones c
						inner join reproducciones r	on r.id_cancion = c.id
						inner join album_cancion ac	on ac.id_cancion = c.id
						inner join albumes al on al.nombre = ac.id_album
					where r.fecha >= fecha_i
					and r.fecha <= fecha_f
					group by al.genero;
end;
$$
language 'plpgsql';

select repro_genero('2021-01-01', '2021-05-02');

create or replace function canciones_repro_unArtista(artista_i varchar)
returns table(cancion_f varchar, repro_count int8) as $$
begin
	return query	select c.cancion, count(r)
					from canciones c
						inner join reproducciones r	on r.id_cancion = c.id
						and c.artista = artista_i
					group by c.cancion
					order by count(r);
end;
$$
language 'plpgsql';

select canciones_repro_unArtista('Drake');

create table bitacora(
funcion tipo_funcion not null,
tabla varchar not null,
registro text not null,
fecha timestamp not null
);

drop table bitacora;
select * from bitacora;

CREATE TYPE tipo_funcion AS ENUM (
    'INSERT',
    'UPDATE',
    'DELETE'
);

drop function ops_sistema;
create function ops_sistema()
returns trigger as $$
declare Funcion VARCHAR := TG_OP;
declare Tabla VARCHAR := TG_TABLE_NAME;
begin
	CASE Funcion
    	WHEN 'INSERT' THEN
        	Funcion = 'INSERT';
	        INSERT INTO bitacora VALUES (CAST(Funcion AS tipo_funcion), Tabla, (CAST(new.* AS text)), localtimestamp);
        WHEN 'UPDATE' THEN   
            Funcion = 'UPDATE';
            INSERT INTO bitacora VALUES (CAST(Funcion AS tipo_funcion), Tabla, (CAST(old.* AS text)), localtimestamp);
        WHEN 'DELETE' THEN   
            Funcion = 'DELETE';
            INSERT INTO bitacora VALUES (CAST(Funcion AS tipo_funcion), Tabla, (CAST(old.* AS text)), localtimestamp);
    	ELSE
            RAISE EXCEPTION 'FUNCION NO DEFINIDA';
    END CASE;
	
	return new;
end;
$$
language 'plpgsql';

drop trigger bitacora_usuario on usuario;
create trigger bitacora_usuario
after insert or update or delete
on usuario
for each row
execute procedure ops_sistema();

drop trigger bitacora_artistas on artistas;
create trigger bitacora_artistas
after insert or update or delete
on artistas
for each row
execute procedure ops_sistema();

drop trigger bitacora_albumes on albumes;
create trigger bitacora_albumes
after insert or update or delete
on albumes
for each row
execute procedure ops_sistema();

drop trigger bitacora_playlist on playlist;
create trigger bitacora_playlist
after insert or update or delete
on playlist
for each row
execute procedure ops_sistema();

drop trigger bitacora_canciones on canciones;
create trigger bitacora_canciones
after insert or update or delete
on canciones
for each row
execute procedure ops_sistema();

insert into usuario values ('user7', 'abcdef', 95, false, false, 3, true);
update usuario set logins = 30, suscripcion = true , id_tipo_admin = 2, activado = true where usuario = 'user6';
delete from usuario where usuario = 'user7';
select * from usuario;
select * from bitacora;

insert into artistas values ('artista1', 'user7');
update artistas set nombre = 'artist1' where nombre = 'artista1';
delete from artistas where nombre = 'artist1';
select * from artistas;
select * from bitacora;

insert into albumes values ('album1', 'Salsa', 'artista1', '2021-05-12', true);
update albumes set genero = 'Pop', fecha_salida = '2021-05-11', activo = false where nombre = 'album1';
delete from albumes where nombre = 'album1';
select * from albumes;
select * from bitacora;

insert into playlist(nombre, nombre_usuario) values ('playlist6', 'user6');
update playlist set nombre = 'playlis6', nombre_usuario = 'user7' where id = 6;
delete from playlist where id = 6;
select * from playlist;
select * from bitacora;

insert into canciones(cancion, link, artista, activa) values ('cancion1', 'https://www.youtube.com', 'artista1', true);
update canciones set cancion = 'cancio1', link = 'youtube', activa = false where id = 6;
delete from canciones where id = 6;
select * from canciones;
select * from bitacora;



select * from AlbumXdia;

CREATE VIEW AlbumXdia AS
--album reproduccion x dia
select albumes.nombre,reproducciones.fecha, count(albumes.nombre) as reproXdia
from ((albumes
inner join album_cancion on album_cancion.Id_album = albumes.nombre)
inner join reproducciones on reproducciones.Id_cancion = album_cancion.Id_cancion)
group by albumes.nombre, reproducciones.fecha;

CREATE VIEW GeneroXdia AS
--genero reproduccion x dia
select albumes.genero,reproducciones.fecha, count(albumes.genero) as reproXdia
from ((albumes
inner join album_cancion on album_cancion.Id_album = albumes.nombre)
inner join reproducciones on reproducciones.Id_cancion = album_cancion.Id_cancion)
group by albumes.genero, reproducciones.fecha;

CREATE VIEW UsuarioXdia AS
--usuario reproduccion x dia
select reproducciones.usuario, reproducciones.fecha,
count(reproducciones.usuario) as repro_dia
from reproducciones
group by reproducciones.usuario, reproducciones.fecha
order by reproducciones.fecha;

CREATE VIEW ArtistaXdia AS
--artista artista x dia
select canciones.artista,reproducciones.fecha as fecha_reproduccion,
count(reproducciones.Id_cancion) as reproducciones
from canciones
inner join reproducciones on reproducciones.Id_cancion = canciones.Id
group by canciones.artista,reproducciones.fecha
order by reproducciones.fecha,count(reproducciones.Id_cancion);


CREATE VIEW Album_Artista_Reproduccion_x_dia AS
select albumes.nombre as Album_Nombre, albumes.creador as Artista_del_Album,
reproducciones.fecha, count(album_cancion.Id_album) as reproAlbumxArtista
from ((albumes
inner join album_cancion on album_cancion.Id_album = albumes.nombre)
inner join reproducciones on reproducciones.Id_cancion = album_cancion.Id_cancion)
group by albumes.nombre,reproducciones.fecha;