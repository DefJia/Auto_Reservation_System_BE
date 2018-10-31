from Book import Book
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('.config.ini')


def detect(num=-1):
    """
    :param num: default: -1(all), the amount of accounts will be detected.
    :return: -1: error, cal: the amount of available accounts.
    """
    user = cfg.get('Account', 'zombieu').split(',')
    pwd = cfg.get('Account', 'zombiep').split(',')
    if len(user) != len(pwd): return -1
    if num > len(user): num = len(user)
    loop = (len(user) if num == -1 else num)
    flag = list()
    for i in range(loop):
        res = Book(user[i], pwd[i]).login()
        if res == {}: flag.append(i)
    cal = loop - len(flag)
    if len(flag) > 0:
        for elem in reversed(flag):
            user.pop(elem)
            pwd.pop(elem)
        cfg.set('Account', 'zombieu', ','.join(user))
        cfg.set('Account', 'zombiep', ','.join(pwd))
        with open('.config.ini', 'w') as configfile:
            cfg.write(configfile)
    return cal


if __name__ == '__main__':
    a = detect()
    print("测试%d个僵尸帐号完毕" % a)
