import requests, time, datetime, json
from bs4 import BeautifulSoup
from configparser import ConfigParser
from collections import OrderedDict

cfg = ConfigParser()
cfg.read('.config.ini', encoding='utf8')

init_url = 'http://seat.lib.bit.edu.cn'
login_url = 'http://login.bit.edu.cn/cas/login'
seat_url = init_url + '/CAS/docs/examples/cas_simple_login.php'


class Book:
    """
        Description here.
    """
    @staticmethod
    def index(first, second=-1):
        """
        :param first:
        :param second:
        :return:
        """
        if second == -1:
            if type(first) == str:
                hash = cfg.get('Account', 'common_hash').split(',').index(first)
                username = cfg.get('Account', 'commonu').split(',')[hash]
                password = cfg.get('Account', 'commonp').split(',')[hash]
                return username, password
            else:
                zombieu = cfg.get('Account', 'zombieu').split(',')
                zombiep = cfg.get('Account', 'zombiep').split(',')
                if first < 0: first = 0
                elif first >= min(len(zombieu), len(zombiep)):
                    first = min(len(zombieu), len(zombiep))
                username = zombieu[first]
                password = zombiep[first]
                return username, password
        else:
            return first, second

    def __init__(self, username, password=-1):
        """
            Description here.
        """
        self.username, self.password = self.index(username, password)
        # self.password = password
        # self.username = username
        self.session = requests.session()
        self.url = ''
        self.post = dict()

    def login(self):
        """
        :return: cookies
        """
        self.session.get(init_url)
        r = self.session.get(login_url)
        soup = BeautifulSoup(r.text, 'html5lib')
        data = dict()
        data['username'] = self.username
        data['password'] = self.password
        for elem in soup.find_all('input')[4:8]:
            data[elem.attrs['name']] = elem.attrs['value']
        self.session.post(login_url, params=data)
        r = self.session.get(seat_url)
        soup = BeautifulSoup(r.text, 'html5lib')
        login_url3 = init_url + soup.find('script').text[14:85]
        r = self.session.get(login_url3)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if r.text[1] == '<':
            print("%s 登录成功 (%s)" % (current_time, self.username))
            return self
        else:
            print("%s 登录失败 (%s)" % (current_time, self.username))
            return {}
        # soup = BeautifulSoup(r.text, 'html5lib')
        # url = self.login_url + soup.find('script').text[14:85]
        # self.session.get(login)

    def prepare(self, room, seat, date):
        """
        :param room: 311, ns1...
        :param seat: A-I / 1-9
        :param date: 0 -> today, 1 -> tomorrow
        :return: -1 -> wrong input, 1 -> run properly
        """
        who_in = [3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 16, 17, 20, 22, 23, 24, 25, 27, 28, 29, 30, 32, 33, 34]
        item_no = dict()
        item_no['ns1'] = {'area_no': 4, 'seat_amount': 55, 'start_no': 655}
        item_no[311] = {'area_no': 17, 'seat_amount': 9, 'start_no': 960}
        item_no[308] = {'area_no': 17, 'seat_amount': 9, 'start_no': 951}
        item_no[211] = {'area_no': 16, 'seat_amount': 9, 'start_no': 942}
        item_no[208] = {'area_no': 16, 'seat_amount': 9, 'start_no': 933}
        item_no[4] = {'area_no': 34, 'seat_amount': 204, 'start_no': 2393}
        diff = abs(datetime.date.today() - datetime.date(2017, 11, 2)).days + date

        if room not in item_no:
            return -1
        room_info = item_no[room]
        segment = 87444 + diff + 731 * who_in.index(room_info['area_no'])
        seat = room_info['start_no'] + int(seat)

        self.url = 'http://seat.lib.bit.edu.cn/api.php/spaces/%s/book' % seat
        cookies = self.session.cookies.get_dict()
        self.post = {'access_token': cookies['access_token'], 'userid': cookies['userid'], 'segment': segment, 'type': 1}
        return self

    def book(self):
        r = self.session.post(self.url, params=self.post)
        try:
            d = json.loads(r.text)
        except json.decoder.JSONDecodeError:
            d = json.loads(r.text[1:])
        try:
            ts = d['data']['_hash_']['expire']
            msg = d['msg']
            server_time = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            current_time = server_time - datetime.timedelta(hours = 1)
            print("%s %s" % (str(current_time), msg))
            if '预约失败' in msg:
                return 2
            else:
                return 1
        except KeyError:
            return -2


if __name__ == '__main__':
    test = Book('ljq').login()
    test = test.prepare(311, 5, 1)
    test.book()
