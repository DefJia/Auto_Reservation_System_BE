from Book import Book
from Query import Query
import time
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('.config.ini', encoding='utf8')


if __name__ == '__main__':
    target_users = cfg.get('_Pick_seat', 'target_users').split(',')
    target_rooms = cfg.get('_Pick_seat', 'target_rooms').split(',')
    date = cfg.getint('_Pick_seat', 'date')
    sleep_second = cfg.getint('_Pick_seat', 'interval')
    cur = 0
    while target_users:
        for room in target_rooms:
            query = Query(date, room)
            res = query.get_list()
            if res:
                for elem in res:
                    account = Book(target_users[0]).login()
                    account.prepare(elem[0], elem[1], date)
                    account.book()
                    del target_users[0]
        time.sleep(sleep_second)
