from Manage import Manage
from Book import Book
import sqlite3


class Crawl:
    @staticmethod
    def crawl_user():
        a = Manage().login()
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        for i in range(69, 2047):
            info = a.query_info('user', page=i)
            for elem in info:
                sql = "insert into user(sid, cid, name, type, department) values ("
                for field in elem:
                    sql += "'" + elem[field] + "',"
                sql = sql[:-1] + ')'
                try:
                    c.execute(sql)
                except sqlite3.IntegrityError:
                    print(sql)
                except sqlite3.OperationalError:
                    print(sql)
            conn.commit()
            print("第%d页完成爬取" % i)
        conn.close()

    @staticmethod
    def crawl_book():
        a = Manage().login()
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        for i in range(3270, 4550):
            info = a.query_info('book', page=i)
            for elem in info:
                sql = "insert into book(bid, sid, name, room, start, end, status, book_time) values ("
                for field in elem:
                    sql += "'" + elem[field] + "',"
                sql = sql[:-1] + ')'
                # print(elem)
                try:
                    c.execute(sql)
                except sqlite3.IntegrityError:
                    print(sql)
                except sqlite3.OperationalError:
                    print(sql)
            conn.commit()
            print("第%d页完成爬取" % i)
        conn.close()
