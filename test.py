from Book import Book
from Query import Query
from Manage import Manage
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
    '''
    a = Manage().login()
    test = Book('ljq').login()
    test = test.prepare(311, 2, 1)
    a.del_book(1120132559, 1)
    test.book()
    '''