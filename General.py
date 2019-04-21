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
    def index(self, first, second=-1):
        cfg_list = self.get_config()
        cfg = cfg_list[0]
        if second == -1:
            hash = cfg.get('Account', 'common_hash').split(',').index(first)
            username = cfg.get('Account', 'commonu').split(',')[hash]
            password = cfg.get('Account', 'commonp').split(',')[hash]
            return username, password
        else:
            return first, second


if __name__ == '__main__':
    a = General()
    a.get_config()

