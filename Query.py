import datetime
import json
import requests
from configparser import ConfigParser


class Query:
    """
        To query available seats on specified date and room.
    """

    def __init__(self, date, room_id):
        """
        :param date: 0 -> today, 1 -> tomorrow
        :param room_id: 211, 308, 311, 208
        :return code, list -> when code > 0, which means code = len(list), query results.
        """
        self.cfg = ConfigParser()
        self.cfg.read('.config.ini', encoding='utf8')
        self.room_id = room_id
        self.area_nos = self.cfg.get('Index', 'area_no').split(',')
        self.room_ids = self.cfg.get('Index', 'room_id').split(',')
        index = self.room_ids.index(str(room_id))
        self.area_no = self.area_nos[index]
        self.date = date
        self.res = list()

    def get_list(self):
        url = 'http://10.1.123.155/api.php/spaces_old'
        params = {'area': self.area_no, 'endTime': '22:40'}
        time_ = datetime.datetime.now() + datetime.timedelta(days=self.date)
        params['day'] = time_.strftime('%Y-%m-%d')
        params['startTime'] = '8:00' if self.date > 0 or datetime.datetime.now().hour < 8 else time_.strftime('%H:%M')
        # The next day or 8:00am before the current day -> 8:00
        try:
            r = requests.get(url, params = params)
        except:
            return None
        d = None
        try:
            d = json.loads(r.text[1:], encoding='utf8')
        except:
            d = json.loads(r.text, encoding='utf8')
        finally:
            if type(d) == dict:
                data = d['data']['list']
                for elem in data:
                    if elem['status'] == 1:
                        # 可预约
                        if len(elem['name']) == 5:
                            # 形如311-A
                            room_id = elem['name'][:3]
                            seat_no = ord(elem['name'][-1]) - 64
                        else:
                            room_id = self.room_id
                            seat_no = int(elem['name'])
                        self.res.append((room_id, seat_no))
                return self.res
            else:
                return None


if __name__ == '__main__':
    cur = Query(0, 'ns1')
    print(cur.get_list())
