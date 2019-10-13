import requests
from Book import Book
from General import General
from Notify import Output
import time, datetime

class Test:
    while True:
        url = 'http://seat.lib.bit.edu.cn/'
        try:
            r = requests.get(url)
            a = r.text
        except:
            a = 315
        if len(a) != 315:
            method_name = '_Book_seat'
            cfg = General.get_config()[0]
            notify_type = cfg.get(method_name, 'notify_type')
            target_users = cfg.get(method_name, 'target_names').split(',')
            target_seats = cfg.get(method_name, 'target_seats').split(',')
            target_rooms = cfg.get(method_name, 'target_rooms').split(',')
            date = cfg.getint(method_name, 'date')

            output = Output()
            text = format('网络修复！')
            output.final_output(text, notify_type)

            for i in range(min(len(target_rooms), len(target_seats), len(target_users))):
                book = Book(target_users[i])
                book = book.prepare(target_rooms[i], target_seats[i], date)
                book.book()
            text = format('预约成功')
            output.final_output(text, notify_type)
            break
        print(datetime.datetime.now())
        time.sleep(5)