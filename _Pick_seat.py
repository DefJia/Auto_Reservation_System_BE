from Book import Book
from Query import Query
import time

if __name__ == '__main__':
    date = 0
    cur = 0
    while True:
        query = Query(date, 311)
        res = query.get_list()
        if res:
            for elem in res:
                account = Book(cur).login()
                account.prepare(elem[0], elem[1], date)
                account.book()
                cur += 1
        time.sleep(1)
