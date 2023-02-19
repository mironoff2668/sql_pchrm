create table if not exists MusicGenre (
	genre_id SERIAL primary key,
	name varchar(60) not null
);

create table if not exists MusicArtist (
	artist_id SERIAL primary key,
	name varchar(60) not null
);

create table if not exists MusicAlbum (
	album_id SERIAL primary key,
	name varchar(60) not null,
	release date
);

create table if not exists MusicTrack(
	track_id SERIAL primary key,
	album_id integer not null references MusicAlbum(album_id),
	name varchar(60) not null,
	duration time
);

create table if not exists ArtistGenre(
	genre_id INTEGER references MusicGenre(genre_id),
	artist_id INTEGER references MusicArtist(artist_id),
	constraint pk primary key (genre_id, artist_id)
);

create table if not exists ArtistAlbum(
	artist_id INTEGER references MusicArtist(artist_id),
	album_id INTEGER references MusicAlbum(album_id),
	constraint fk primary key (artist_id, album_id)
);

create table if not exists Collection(
	collection_id SERIAL primary key,
	name varchar(60) not null,
	year_release date not null
);

create table if not exists CollectionTrack(
	id SERIAL primary key,
	collection_id INTEGER not null references Collection(collection_id),
	track_id INTEGER not null references MusicTrack(track_id)
);