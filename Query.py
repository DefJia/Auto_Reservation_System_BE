import datetime
import json
import requests


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
        self.date = date
        self.area_id = 17 if room_id > 300 else 16
        self.res = list()

    def get_list(self):
        url = 'http://10.1.123.155/api.php/spaces_old'
        params = {'area': self.area_id, 'endTime': '22:40'}
        time_ = datetime.datetime.now() + datetime.timedelta(days=self.date)
        params['day'] = time_.strftime('%Y-%m-%d')
        params['startTime'] = '8:00' if self.date > 0 or datetime.datetime.now().hour < 8 else time_.strftime('%H:%M')
        # The next day or 8:00am before the current day -> 8:00
        try: r = requests.get(url, params = params)
        except: return None
        d = None
        try: d = json.loads(r.text[1:], encoding='utf8')
        except: d = json.loads(r.text, encoding='utf8')
        finally:
            if type(d) == dict:
                data = d['data']['list']
                for elem in data:
                    if elem['status'] == 1:
                        room_id = int(elem['name'][:3])
                        seat_no = ord(elem['name'][-1]) - 64
                        self.res.append((room_id, seat_no))
                return self.res
            else:
                return None


if __name__ == '__main__':
    cur = Query(0, 17)
    print(cur.get_list())
