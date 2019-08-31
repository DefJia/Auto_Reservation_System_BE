from Book import Book
from General import General


if __name__ == '__main__':
    cfg = General.get_config()[0]
    target_users = cfg.get('_Book_seat', 'target_names').split(',')
    target_rooms = cfg.get('_Book_seat', 'target_rooms').split(',')
    target_seats = cfg.get('_Book_seat', 'target_seats').split(',')
    date = cfg.getint('_Book_seat', 'date')
    for i in range(min(len(target_rooms), len(target_seats), len(target_users))):
        book = Book(target_users[i])
        book = book.prepare(target_rooms[i], target_seats[i], date)
        book.book()
