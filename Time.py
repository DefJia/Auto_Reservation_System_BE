import datetime
import time, requests


class Time:
    @staticmethod
    def wait_until(time_):
        """
        It needs to be clarified that the time is that on remote server.
        :return: 0 -> time is up
        """

    @staticmethod
    def get_server_time(host):
        r = requests.get(host)
        _t = str(r.headers)[15:35]
        t = datetime.datetime.strptime(_t, "%d %b %Y %H:%M:%S") + datetime.timedelta(hours=8)
        return t


if __name__ == '__main__':
    host = 'http://seat.lib.bit.edu.cn'
    res = Time()
    r = res.get_server_time(host)
    print(r)
