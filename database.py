import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''create table user
        (id int auto increment primary key,
	sid int(10),
	cid int(10),
	name varchar(10),
	type varchar(10),
	department varchar(10)
);''')