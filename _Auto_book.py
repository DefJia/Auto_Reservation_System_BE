from Time import Time
from Book import Book
import datetime
from General import General


if __name__ == '__main__':
    cfg = General.get_config()[0]
    type = cfg.getint('_Auto_book', 'type')
    target_name = cfg.get('_Auto_book', 'target_name')
    target_room = cfg.get('_Auto_book', 'target_room')
    target_seat = cfg.getint('_Auto_book', 'target_seat')
    max_try_times = cfg.getint('_Auto_book', 'max_try_times')
    date = 0 if type in (1, 2) else 1
    t = Time()
    if type in (0, 1): t.time_control(type)  # 时间控制
    b = Book(target_name).prepare(target_room, target_seat, date)
    flag = 0  # 是否预约成功
    cnt = 0  # 发送请求次数
    while flag != 1 and cnt < max_try_times:
        flag = b.book()
        print(datetime.datetime.now())
        cnt += 1
