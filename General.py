import os
from configparser import ConfigParser
from collections import OrderedDict
import platform


class General:
    @staticmethod
    def get_config():
        config_lst = list()
        env = platform.system()
        split_sign = '\\' if env == 'Windows' else '/'
        cwd_raw = os.getcwd()
        cfg = ConfigParser()
        cfg.read(cwd_raw + split_sign + '.config.ini', encoding='utf-8')
        cwd_lst = cwd_raw.split(split_sign)
        config_lst.append(cfg)
        if cwd_lst[-1] == 'Advanced':
            cwd_root = cwd_raw[:-(len(cwd_lst[-1])+1)]
            cfg = ConfigParser()
            cfg.read(cwd_root + split_sign + '.config.ini', encoding='utf-8')
            config_lst = [cfg] + config_lst
        return config_lst

    @staticmethod
    def index(first, second=-1):
        """
        :param first:
        :param second:
        :return:
        三种可能性：
            1. 单个参数，人名缩写
            2. 单个参数，僵尸账号序号
            3. 两个参数，账号和密码（临时）
        返回两个参数————用户名和密码
        """
        cfg = General.get_config()
        cfg_main = cfg[0]
        if second == -1:
            if type(first) == str:
                # 第一种情况
                hash = cfg_main.get('Account', 'common_hash').split(',').index(first)
                username = cfg_main.get('Account', 'commonu').split(',')[hash]
                password = cfg_main.get('Account', 'commonp').split(',')[hash]
                return username, password
            else:
                zombieu = cfg_main.get('Account', 'zombieu').split(',')
                zombiep = cfg_main.get('Account', 'zombiep').split(',')
                if first < 0:
                    first = 0
                elif first >= min(len(zombieu), len(zombiep)):
                    first = min(len(zombieu), len(zombiep)) - 1
                username = zombieu[first]
                password = zombiep[first]
                return username, password
        else:
            return first, second


if __name__ == '__main__':
    a = General()
    a.get_config()
