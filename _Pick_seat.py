from Book import Book
from Query import Query
import time
from datetime import datetime
from General import General

cfg = General.get_config()[0]

if __name__ == '__main__':
    target_users = cfg.get('_Pick_seat', 'target_users').split(',')
    target_rooms = cfg.get('_Pick_seat', 'target_rooms').split(',')
    date = cfg.getint('_Pick_seat', 'date')
    sleep_second = cfg.getint('_Pick_seat', 'interval')
    cur = 0
    while len(target_users):
        for room in target_rooms:
            query = Query(date, room)
            res = query.get_list()
            if res:
                for elem in res:
                    account = Book(target_users[0])
                    account.prepare(elem[0], elem[1], date)
                    account.book()
                    del target_users[0]
                    if not target_users:
                        cur = -1
                        break
            if cur > 0:
                cur += 1
                print('第%d次查询，%s次列车无余票，时间%s...' % (cur, room, str(datetime.now())[:-7]))
                time.sleep(sleep_second)
            else:
                break
