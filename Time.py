import datetime
import time
import requests
from configparser import ConfigParser
import ast


class Time:
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('.config.ini', encoding='utf8')

    def wait_until(self, type):
        """
        It needs to be clarified that the time is that on remote server.
        :return: 0 -> time is up
        """
        pass

    def time_control(self, type):
        """
        :param type: 0 -> pre_book, 1 -> pick
        :return:
        """
        tmp = 'book' if type == 0 else 'pick'
        target_time = self.cfg.get('Time', tmp + '_time').split(':')
        hour = int(target_time[0])
        minute = int(target_time[1])
        prepare_seconds = self.cfg.getint('Time', 'advanced_second_to_prepare')
        interval_seconds = self.cfg.getint('Time', 'interval_second_to_calibrate')
        start_seconds = self.cfg.getint('Time', 'advanced_second_to_book')
        while True:
            if self.cal_seconds(0, (hour, minute), prepare_seconds):
                while not self.cal_seconds(1, (hour, minute), start_seconds):
                    time.sleep(interval_seconds)
                return 0
            else:
                time.sleep(interval_seconds)

    def cal_seconds(self, time_type, target_time, target_delta_seconds):
        """
        :param time_type: 0 -> local time, 1 -> server time
        :param target_time: target time tuple -> (hour, minute)
        :param target_delta_seconds: target delta seconds
        :return: true or false
        """
        target_seconds = (target_time[0] * 60 + target_time[1]) * 60
        current_time = datetime.datetime.now() if time_type == 0 else self.get_server_time()
        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second
        current_seconds = current_hour * 3600 + current_minute * 60 + current_second
        current_delta_second = target_seconds - current_seconds
        print('模式%d, 时间差%d' % (time_type, current_delta_second))
        return True if 0 <= current_delta_second <= target_delta_seconds else False

    @staticmethod
    def get_server_time():
        host = 'http://seat.lib.bit.edu.cn'
        r = requests.get(host)
        dic = ast.literal_eval(str(r.headers))
        t = datetime.datetime.strptime(dic['Date'], "%a, %d %b %Y %H:%M:%S GMT") + datetime.timedelta(hours=8)
        return t


if __name__ == '__main__':
    res = Time()
    # r = res.time_control(0)
    r = res.get_server_time()
    print(r)
