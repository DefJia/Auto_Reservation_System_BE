from General import General
import requests, time, datetime, json
from bs4 import BeautifulSoup
from configparser import ConfigParser


class Book:
    """
        预约类
    """
    def __init__(self, username, password=-1):
        configs = General.get_config()
        self.cfg_main = configs[0]
        self.init_url = self.cfg_main.get('Site_url', 'init_url')
        self.login_url = self.cfg_main.get('Site_url', 'login_url')
        self.seat_url = self.init_url + self.cfg_main.get('Site_url', 'seat_url')
        # Get urls
        self.room_ids = self.cfg_main.get('Index', 'room_id').split(',')
        self.area_nos = self.cfg_main.get('Index', 'area_no').split(',')
        self.start_nos = self.cfg_main.get('Index', 'start_no').split(',')
        self.room_list = self.cfg_main.get('Index', 'room_list').split(',')
        self.base_para = self.cfg_main.getint('Index', 'base_para')
        self.delta_para = self.cfg_main.getint('Index', 'delta_para')
        # Get indexes
        self.username, self.password = General.index(username, password)
        self.session = requests.session()
        self.url = ''
        self.post = dict()
        # Preparations
        self.login()

    def login(self):
        """
        :return: cookies
        """
        self.session.get(self.init_url)
        r = self.session.get(self.login_url)
        soup = BeautifulSoup(r.text, 'html5lib')
        data = dict()
        data['username'] = self.username
        data['password'] = self.password
        for elem in soup.find_all('input')[4:8]:
            data[elem.attrs['name']] = elem.attrs['value']
        self.session.post(self.login_url, params=data)
        r = self.session.get(self.seat_url)
        soup = BeautifulSoup(r.text, 'html5lib')
        login_url3 = self.init_url + soup.find('script').text[14:85]
        r = self.session.get(login_url3)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if r.text[1] == '<':
            print("%s 登录成功 (%s)" % (current_time, self.username))
            return self
        else:
            print("%s 登录失败 (%s)" % (current_time, self.username))
            return {}

    def prepare(self, room, seat, date):
        """
        :param room: 311, ns1...
        :param seat: A-I / 1-9
        :param date: 0 -> today, 1 -> tomorrow
        :return: -1 -> wrong input, 1 -> run properly
        """
        """
        who_in = [3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 16, 17, 20, 22, 23, 24, 25, 27, 28, 29, 30, 32, 33, 34]
        item_no = dict()
        item_no[1] = {'area_no': 4, 'seat_amount': 55, 'start_no': 655}
        item_no['311'] = {'area_no': 17, 'seat_amount': 9, 'start_no': 960}
        item_no['308'] = {'area_no': 17, 'seat_amount': 9, 'start_no': 951}
        item_no[211] = {'area_no': 16, 'seat_amount': 9, 'start_no': 942}
        item_no[208] = {'area_no': 16, 'seat_amount': 9, 'start_no': 933}
        item_no['4'] = {'area_no': 34, 'seat_amount': 204, 'start_no': 2393}
        """
        diff = abs(datetime.date.today() - datetime.date(2017, 11, 2)).days + date
        index = self.room_ids.index(str(room))
        area_no = self.area_nos[index]
        segment = self.base_para + diff + self.delta_para * self.room_list.index(area_no)
        seat = int(self.start_nos[index]) + int(seat)
        self.url = 'http://seat.lib.bit.edu.cn/api.php/spaces/%s/book' % seat
        cookies = self.session.cookies.get_dict()
        self.post = {'access_token': cookies['access_token'], 'userid': cookies['userid'], 'segment': segment, 'type': 1}
        return self

    def book(self):
        available = self.check_available()
        if not available:
            return -3   
        r = self.session.post(self.url, params=self.post)
        try:
            d = json.loads(r.text)
        except json.decoder.JSONDecodeError:
            d = json.loads(r.text[1:])
        try:
            ts = d['data']['_hash_']['expire']
            # TypeError: 'NoneType' object is not subscriptable
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
        except TypeError:
            return -2

    def check_available(self):
        sections = self.cfg_main.sections()
        if 'Others' in sections and self.cfg_main.get('Others', 'HasAdvanced') == 'True':
            from Advanced.Available import CheckAvailable
            cur = CheckAvailable(self.username)
            a = cur.set_available() if not cur.is_available() else True
            return a
        else:
            return True


if __name__ == '__main__':
    test = Book('jzh')
