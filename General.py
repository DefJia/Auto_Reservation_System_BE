import sqlite3
import os
from configparser import ConfigParser
from collections import OrderedDict
import platform


class General:
    @staticmethod
    def del_reneges(para=-1):
        target_group = 'common' if type(para) == int and para == -1 else 'zombie'
        a = Manage().login()
        lst = cfg.get('Account', target_group+'u').split(',')
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

    @staticmethod
    def get_config():
        config_lst = list()
        env = platform.system()
        split_sign = '\\' if env == 'Windows' else '/'
        cwd_raw = os.getcwd()
        cfg = ConfigParser()
        cfg.read(cwd_raw + split_sign + '.config.ini')
        cwd_lst = cwd_raw.split(split_sign)
        config_lst.append(cfg)
        if cwd_lst[-1] == 'Advanced':
            cwd_root = cwd_raw[:-(len(cwd_lst[-1])+1)]
            cfg = ConfigParser()
            cfg.read(cwd_root + split_sign + '.config.ini')
            config_lst = [cfg] + config_lst
        return config_lst


if __name__ == '__main__':
    a = General()
    a.get_config()

