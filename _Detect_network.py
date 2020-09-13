import requests
from Book import Book
from General import General
from Notify import Output
import time, datetime, requests

class Test:
    def __init__(self):
        configs = General.get_config()
        self.cfg_main = configs[0]
        self.init_url = self.cfg_main.get('Site_url', 'init_url')

    def if_response(self):
        try:
            r = requests.get(self.init_url, timeout=5)
        except:
            print(datetime.datetime.now())
            time.sleep(5)
            return self.if_response()
        else:
            print('网络修复！')
            output = Output()
            output.final_output('网络修复', 45)
            return 0

    def if_availiable(self):
        pass

if __name__ == "__main__":
    a = Test()
    a.if_response()

'''
    while True:
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
        '''