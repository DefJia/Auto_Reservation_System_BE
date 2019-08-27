from Time import Time
from Book import Book
import datetime
from General import General


if __name__ == '__main__':
    t = Time()
    cfg = General.get_config()[0]
    type = cfg.getint('_Auto_book', 'type')
    if type in (0, 1):
        t.time_control(type)
    target_name = cfg.get('_Auto_book', 'target_name')
    target_room = cfg.get('_Auto_book', 'target_room')
    target_seat = cfg.getint('_Auto_book', 'target_seat')
    date = 0 if type in (1, 2) else 1
    b = Book(target_name).prepare(target_room, target_seat, date)
    flag = 0  # 是否预约成功
    cnt = 0  # 发送请求次数
    max_try_times = cfg.getint('_Auto_book', 'max_try_times')
    while flag != 1 and cnt < max_try_times:
        flag = b.book()
        print(datetime.datetime.now())
        cnt += 1
