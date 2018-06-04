create table user(
	id integer primary key autoincrement,
	sid int(10) unique,
	cid int(10) unique,
	name varchar(10),
	type varchar(10),
	department varchar(10)
);
create table book(
	id integer primary key autoincrement,
	bid int(12),
	sid int(10),
	name varchar(10),
	room varchar(20),
	start timestamp,
	end timestamp,
	status varchar(10),
	book_time timestamp,
	note varchar
);
