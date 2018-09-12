from Manage import Manage
from Book import Book
import sqlite3
from configparser import ConfigParser
from collections import OrderedDict

cfg = ConfigParser()
cfg.read('.config.ini')


class General:
    @staticmethod
    def del_reneges():
        a = Manage().login()
        lst = cfg.get('Account', 'commonu').split(',')
        for elem in lst:
            a.del_renege(elem)

    @staticmethod
    def index(first, second=-1):
        if second == -1:
            hash = cfg.get('Account', 'common_hash').split(',').index(first)
            username = cfg.get('Account', 'commonu').split(',')[hash]
            password = cfg.get('Account', 'commonp').split(',')[hash]
            return username, password
        else:
            return first, second

    @staticmethod
    def transfer():
        username, password = General.index('wyi')
        b = Book(username, password).login().prepare(4, 147, 0)
        a = Manage().login().del_book(1120153332, 0)
        b.book()


if __name__ == '__main__':
    General.transfer()
    # crawl_book()
    # del_reneges()
