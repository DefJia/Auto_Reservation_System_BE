from Book import Book
from General import General
from Notify import Output


if __name__ == '__main__':
    method_name = '_Book_seat'
    cfg = General.get_config()[0]
    notify_type = cfg.get(method_name, 'notify_type')
    target_users = cfg.get(method_name, 'target_names').split(',')
    target_seats = cfg.get(method_name, 'target_seats').split(',')
    target_rooms = cfg.get(method_name, 'target_rooms').split(',')
    date = cfg.getint(method_name, 'date')

    output = Output()

    for i in range(min(len(target_rooms), len(target_seats), len(target_users))):
        book = Book(target_users[i])
        book = book.prepare(target_rooms[i], target_seats[i], date)
        res = book.book()
        while res < 0:
            res = book.book()
        
