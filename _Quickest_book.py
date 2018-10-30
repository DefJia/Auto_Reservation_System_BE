from Time import Time
from Book import Book
import datetime

if __name__ == '__main__':
    t = Time()
    t.time_control(0)
    b = Book('ljq').login().prepare(311, 5, 1)
    flag = 0
    cnt = 0
    while flag != 1 and cnt < 150:
        flag = b.book()
        print(datetime.datetime.now())
        cnt += 1
