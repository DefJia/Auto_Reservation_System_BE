from Time import Time
from Book import Book
import datetime
from General import General
from Notify import Output


if __name__ == '__main__':
    method_name = '_Auto_book'
    cfg = General.get_config()[0]
    notify_type = cfg.get(method_name, 'notify_type')
    type = cfg.getint(method_name, 'type')
    target_name = cfg.get(method_name, 'target_name')
    target_room = cfg.get(method_name, 'target_room')
    target_seat = cfg.getint(method_name, 'target_seat')
    max_try_times = cfg.getint(method_name, 'max_try_times')

    output = Output()
    t = Time()

    date = 0 if type in (1, 2) else 1
    if type in (0, 1): t.time_control(type)  # 时间控制
    b = Book(target_name).prepare(target_room, target_seat, date)
    flag = 0  # 是否预约成功
    cnt = 0  # 发送请求次数
    while flag != 1 and cnt < max_try_times:
        flag = b.book()
        print(datetime.datetime.now())
        cnt += 1
