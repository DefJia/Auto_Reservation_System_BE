from wxpy import *
from configparser import ConfigParser

class Robot:
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('.config.ini', encoding='utf8')
        try:
            self.bot = Bot(cache_path=True, console_qr=2)
        except:
            print('此账号已被列入黑名单，无法登陆！')

    @self.bot.register(my_friend)
    def reply_my_friend(msg):
        return 'received: {} ({})'.format(msg.text, msg.type)


if __name__ == '__main__':
    a = Robot()
