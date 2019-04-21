from Book import Book
from General import General

cfg = General.get_config()[0]

if __name__ == '__main__':
    target_user = cfg.get('_Book_seat', 'target_name')
    book = Book(target_user)
    target_room = cfg.get('_Book_seat', 'target_room')
    target_seat = cfg.getint('_Book_seat', 'target_seat')
    date = cfg.getint('_Book_seat', 'date')
    book = book.prepare(target_room, target_seat, date)
    while True:
        book.book()
