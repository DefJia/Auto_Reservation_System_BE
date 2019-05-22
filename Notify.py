from wxpy import *
from configparser import ConfigParser
from General import General

cfg = General.get_config()[0]

def continuous_output(text):
    print(text)

def final_output(text):
    from_ = cfg.get('Notify', 'Mail_from')
    pwd = cfg.get('Notify', 'Password')
    to = cfg.get('Notify', 'Mail_to')
    mail = Mail(from_, pwd, to)

class Robot:
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('.config.ini', encoding='utf8')
        try:
            self.bot = Bot(cache_path=True, console_qr=2)
        except:
            print('此账号已被列入黑名单，无法登陆！')

    # @self.bot.register(my_friend)
    def reply_my_friend(msg):
        return 'received: {} ({})'.format(msg.text, msg.type)


class Mail:
    def __init__(self, from_, psw, to):
        pass


if __name__ == '__main__':
    a = Robot()
