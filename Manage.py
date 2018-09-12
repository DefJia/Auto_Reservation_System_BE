import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
from collections import OrderedDict
from datetime import *

cfg = ConfigParser()
cfg.read('.config.ini')
main_url = "http://10.1.123.155"


class Manage:
    """
        Description here.
    """

    def __init__(self):
        """ Create a session. """
        self.session = requests.session()

    def login(self):
        login_url = main_url + "/Admin/Public/login"
        username = cfg.get('Manage', 'username')
        password = cfg.get('Manage', 'password')
        data = {'username': username, 'password': password}
        self.session.post(login_url, data=data)
        return self

    def query_info(self, action, student_id='', page=1):
        """
        :param action: 'user', 'book', 'renege'
        :param student_id: int(10)
        :param page: int
        :return: info(list)
        """
        if action == 'user':
            # field = ['学号', '卡号', '姓名', '类型', '部门']
            field = cfg.get('Manage', 'field_user').split(',')
            query_url = main_url + '/Admin/User/index/menuid/17/p/'
        elif action == 'book':
            field = cfg.get('Manage', 'field_book').split(',')
            query_url = main_url + '/Admin/SpaceBook/index/isSingle/1/menuid/28/p/'
        elif action == 'renege':
            field = []
            query_url = main_url + '/Admin/RenegeLog/index/menuid/25/p/'
        else:
            return -1
        flag = 0
        while flag == 0:
            try:
                r = self.session.get(query_url + str(page))
                flag = 1
            except:
                pass
        soup = BeautifulSoup(r.text, 'html5lib')
        trs = soup.find('tbody').find_all('tr')
        info = list()
        for tr in trs:
            tds = tr.find_all('td')
            tmp = OrderedDict()
            for i in range(len(field)):
                if action == 'book' and i == len(field) - 1:
                    tmp[field[i]] = self.get_book_time(tds[i + 1].find('a').get('href'))
                    # 如果为空则为预约机预约
                elif action == 'book' and i == len(field) - 2:
                    tmp[field[i]] = rm_space(tds[i+1].text)
                else:
                    tmp[field[i]] = tds[i + 1].text
            info.append(tmp)
        return info

    def del_renege(self, student_id):
        renege_url = main_url + "/Admin/RenegeLog/index/menuid/25"
        renege_del_url = main_url + "/Admin/RenegeLog/del"
        data = {'renegeUser': student_id}
        r = self.session.post(renege_url, data=data)
        soup = BeautifulSoup(r.text, 'html5lib')
        n = 0
        for i in soup.find_all('input')[8:]:
            n += 1
            data = {'id[]': i.get('value')}
            self.session.post(renege_del_url, data=data)
        print("已删除%s的%d条违约记录" % (student_id, n))
        return n

    def del_book(self, sid, date_delta):
        """
        :param sid:
        :param date_delta: 0 -> today, 1 -> tomorrow
        :return:
        """
        date_str = (date.today() + timedelta(days=date_delta)).strftime("%Y-%m-%d")
        book_url = main_url + '/Admin/SpaceBook/index/keyword/%d/isSingle/1/menuid/28/p/1' % sid
        book_rm_url = main_url + '/Admin/SpaceBook/del'
        r = self.session.get(book_url)
        soup = BeautifulSoup(r.text, 'html5lib')
        trs = soup.find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            try:
                status = rm_space(tds[7].text)
            except IndexError:
                return -1
            else:
                if status in ('预约成功', '预约开始提醒') and tds[5].text[:10] == date_str:
                    target = tds[0].find('input').get('value')
                    data = {'id[]': target}
                    self.session.post(book_rm_url, data=data)
                    print("已删除学号%d在%s的预约" % (sid, date_str))
                    break
        return 0

    def get_book_time(self, href):
        href = main_url + href
        r = self.session.get(href)
        soup = BeautifulSoup(r.text, 'html5lib')
        string = soup.find_all('p', class_='form-control-static')[12].text[:-4]
        return string


def rm_space(string):
    string = string.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
    return string


if __name__ == '__main__':
    a = Manage().login()
    a.del_book(1120153332, 0)
    # a.query_info('book')
    '''
    for sid in lst:
        n = a.del_renege(sid)
        print("Delect %d logs of %d successfully" % (n, sid))
    '''
