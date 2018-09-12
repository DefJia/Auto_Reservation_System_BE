import time
import requests
from bs4 import BeautifulSoup
import json
import threading, datetime

username_ = [1120171424,1120121003,1120122278,1120131094,1120131935,1120132559,1120130606,1120130971,1120131401,1120131551,1120131630,1120131676,1120132348,1120132419,1120133250,1120133276,1120140046,1120140107,1120140296,1120140468,1120140508,1120140640,1120141052,1120141135,1120141148,1120141171,1120141358,1120141456,1120141473,1120141497,1120141624,1120141654,1120141660,1120141674,1120141684,1120141699,1120141985,1120141994,1120142011,1120142014,1120142220,1120142268,1120142275,1120142350,1120142449,1120142609,1120142611,1120142634,1120142644,1120142684,1120142864,1120142919,1120142947,1120143092,1120143121,1120143172,1120143180,1120143300,1120143318,1120143413,1120143424,1120150224,1120150456,1120150512,1120150528,1120150621,1120150714,1120151147,1120151350,1120151406,1120151575,1120151667,1120151766,1120151936,1120151946,1120152133,1120152144,1120152152,1120152155,1120152156,1120152330,1120152340,1120152399,1120152581,1120152586,1120152716,1120152871,1120152949,1120153100,1120153230,1120153253,1120160169,1120160217,1120161227,1120162833,1120163214]
password_ = [1120171424,1120121003,1120122278,123456,123456,123456,1120130606,1120130971,1120131401,1120131551,1120131630,1120131676,1120132348,1120132419,1120133250,1120133276,1120140046,1120140107,1120140296,1120140468,1120140508,1120140640,1120141052,1120141135,1120141148,1120141171,1120141358,1120141456,1120141473,1120141497,1120141624,1120141654,1120141660,1120141674,1120141684,1120141699,1120141985,1120141994,1120142011,1120142014,1120142220,1120142268,1120142275,1120142350,1120142449,1120142609,1120142611,1120142634,1120142644,1120142684,1120142864,1120142919,1120142947,1120143092,1120143121,1120143172,1120143180,1120143300,1120143318,1120143413,1120143424,1120150224,1120150456,1120150512,1120150528,1120150621,1120150714,1120151147,1120151350,1120151406,1120151575,1120151667,1120151766,1120151936,1120151946,1120152133,1120152144,1120152152,1120152155,1120152156,1120152330,1120152340,1120152399,1120152581,1120152586,1120152716,1120152871,1120152949,1120153100,1120153230,1120153253,1120160169,1120160217,1120161227,1120162833,1120163214]
start_no = 10
room_name = [308,308,308,308]
seat_no = [3,6,8,9]

#[1120171424, 1120121003, 1120122278, 1120130580, 1120131094, 1120131935, 1120132559, 1120130606, 1120130971, 1120131401, 1120131551, 1120131630, 1120131676, 1120132348, 1120132419, 1120133250, 1120133276, 1120140046, 1120140107, 1120140296, 1120140468, 1120140508, 1120140640, 1120141052, 1120141096, 1120141135, 1120141148, 1120141171, 1120141358, 1120141456, 1120141473, 1120141497, 1120141624, 1120141654, 1120141660, 1120141674, 1120141684, 1120141699, 1120141985, 1120141994, 1120142011, 1120142014, 1120142220, 1120142268, 1120142275, 1120142350, 1120142449, 1120142609, 1120142611, 1120142634, 1120142644, 1120142684, 1120142864, 1120142919, 1120142947, 1120143092, 1120143121, 1120143172, 1120143180, 1120143300, 1120143318, 1120143413, 1120143424, 1120150224, 1120150456, 1120150512, 1120150528, 1120150621, 1120150714, 1120151147, 1120151350, 1120151406, 1120151575, 1120151667, 1120151766, 1120151936, 1120151946, 1120152133, 1120152144, 1120152152, 1120152155, 1120152156, 1120152330, 1120152340, 1120152399, 1120152581, 1120152586, 1120152656, 1120152716, 1120152871, 1120152949, 1120153100, 1120153230, 1120153253, 1120160169, 1120160217, 1120161227, 1120161391, 1120161435, 1120162077, 1120162290, 1120162833, 1120163214]
#[1120171424, 1120121003, 1120122278, 123456, 123456, 123456, 123456, 1120130606, 1120130971, 1120131401, 1120131551, 1120131630, 1120131676, 1120132348, 1120132419, 1120133250, 1120133276, 1120140046, 1120140107, 1120140296, 1120140468, 1120140508, 1120140640, 1120141052, 1120141096, 1120141135, 1120141148, 1120141171, 1120141358, 1120141456, 1120141473, 1120141497, 1120141624, 1120141654, 1120141660, 1120141674, 1120141684, 1120141699, 1120141985, 1120141994, 1120142011, 1120142014, 1120142220, 1120142268, 1120142275, 1120142350, 1120142449, 1120142609, 1120142611, 1120142634, 1120142644, 1120142684, 1120142864, 1120142919, 1120142947, 1120143092, 1120143121, 1120143172, 1120143180, 1120143300, 1120143318, 1120143413, 1120143424, 1120150224, 1120150456, 1120150512, 1120150528, 1120150621, 1120150714, 1120151147, 1120151350, 1120151406, 1120151575, 1120151667, 1120151766, 1120151936, 1120151946, 1120152133, 1120152144, 1120152152, 1120152155, 1120152156, 1120152330, 1120152340, 1120152399, 1120152581, 1120152586, 1120152656, 1120152716, 1120152871, 1120152949, 1120153100, 1120153230, 1120153253, 1120160169, 1120160217, 1120161227, 1120161391, 1120161435, 1120162077, 1120162290, 1120162833, 1120163214]
hour = 5
min_ = 59
second = 50
_hour = 6
_min_ = 2
_second = 0

#server time
time = []
'''
time.append('0:0:30')#mail 1
time[1] = '5:30:0'#mail 2
time[2] = '5:59:0'#cookies
time[3] = '6:0:0'#requests(strict)
'''

#log
file_ = 'log.txt'
'''
fo = open("runoob.txt", "r+")
str = "6:www.runoob.com"
fo.seek(0, 2)
line = fo.write( str )
'''

#username = [1120153284, 1120152591, 1120153332, 1120130662, 1120153335, 1120153240, 1120171424]
#password = ['jzr31415926535','jiangzhihan', 'wyi1997..', '190211', '657039xhy', 'wsluoheng324', '1120171424']


who_in = [3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 16, 17]
#具体树状结构见Handout1
item_no = {}
#item_no[''] = {'area_no': , 'seat_amount': , 'seat_start_no': }
item_no['ns1'] = {'area_no': 4, 'seat_amount': 55, 'start_no': 655}
item_no[311] = {'area_no': 17, 'seat_amount': 9, 'start_no': 960}
item_no[308] = {'area_no': 17, 'seat_amount': 9, 'start_no': 951}
item_no[211] = {'area_no': 16, 'seat_amount': 9, 'start_no': 942}
item_no[208] = {'area_no': 16, 'seat_amount': 9, 'start_no': 933}

def get_parameter(room_name, seat_no):
    diff = abs(datetime.date.today()-datetime.date(2017, 11, 2)).days
    diff += 0
    #11,1意思是直接定位到下一天
    try:
        a_dic = item_no[room_name]
        #a为segment索引
    except:
        #要对输入做控制
        print('wrong input')
        return 0, 0
    segment = 87444 + diff + 731 * who_in.index(a_dic['area_no'])
    seat = a_dic['start_no'] + int(seat_no)
    #要对seat_no的类型做控制
    return seat, segment

def pre(username, password, seat, segment):
    s = requests.session()
    url1 = 'http://seat.lib.bit.edu.cn'
    url2= 'http://login.bit.edu.cn/cas/login'
    url3 = url1 + '/CAS/docs/examples/cas_simple_login.php'
    #url4 = url1 + '/Api/auto_user_check'
    url5 = url1 + '/CAS/docs/examples/cas_simple_login.php'
    r = s.get(url1)
    r = s.get(url2)
    soup = BeautifulSoup(r.text, 'html5lib')
    data = {}
    data['username'] = username
    data['password'] = password
    for elem in soup.find_all('input')[4:8]:
        data[(elem.attrs)['name']] = (elem.attrs)['value']
    r = s.post(url2, params = data)
    r = s.get(url3)
    r = s.get(url5)
    soup = BeautifulSoup(r.text, 'html5lib')
    url4 = url1 + soup.find('script').text[14:85]
    r = s.get(url4)
    print (str(username) + '登陆成功')
    cookies = s.cookies.get_dict()
    url = 'http://seat.lib.bit.edu.cn/api.php/spaces/%s/book' % seat
    post = {'access_token': cookies['access_token'], \
            'userid': cookies['userid'],\
            'segment': segment,\
            'type': 1}
    return url, post, s

def final(url, post, s):
    r = s.post(url, params = post)
    try:
        d = json.loads(r.text)
        print (1)
        print (r.text)
    except:
        d = json.loads(r.text[1:])
        print (2)
        print (r.text)
    else:
        print (r.text)
        return 0
    try:
        print (d['data']['_hash_']['expire']+'\n')
        if d['status'] == 0:
            print (d['msg']+'\n')
            return 0
        elif d['status'] == -1:
            print (d['msg']+'\n')
            return -1
        else:
            print (d['msg']+'\n')
            return 1
    except:
        return 0

def get_webservertime(host):
    #now_time = datetime.datetime.now()
    r = requests.get(host)
    ts=  str(r.headers)[15:35] #获取http头date部分
    #print(ts)
    #sv_time = datetime.datetime.strptime(ts, "%d %b %Y %H:%M:%S") + \
 #       datetime.timedelta(hours = 8)#将GMT时间转换成北京时间
    # now_time_ = datetime.datetime.now()
    #return sv_time#, now_time_
    #return now_time - bj_time

class myThread (threading.Thread):
    def __init__(self, username, password, seat, segment):
        threading.Thread.__init__(self)
        url, post, s = pre(username, password, seat, segment)
        self.username = username
        self.url = url
        self.post = post
        self.s = s
        #print (s.cookies.get_dict())
    def run(self):
        print ("开始线程：" + str(self.username) + '\n')
        flag = 0
        while True and flag <= 0:  #若8:30为<=0, 记得改info
            flag = final(self.url, self.post, self.s)
            #time.sleep(2)
        print ("退出线程：" + str(self.username) + str(flag))

def start(td):
    while 1:#get_webservertime('http://10.1.123.155').second > 0:
        #print (get_webservertime('http://10.1.123.155'))
        for elem in td:
            try:
                elem.start()
            except:
                pass
        for elem in td:
            elem.join()
        print ("退出主线程")
        return 0


# 创建新线程
flag = 0

td = []
while True:
    while datetime.datetime.now() > datetime.datetime(2017,12,27,5,59,15) and flag==0:
        flag = 1
        no = start_no
        a = 1
        # td = []
        for i in range(len(room_name)):#room
            # for ii in range(len(seat_no)):#seat
            print (a, end='-')
            a += 1
            seat, segment = get_parameter(room_name[i], seat_no[i])
            try:
                thread = myThread(username_[no] ,\
                              password_[no], \
                              seat, segment)
            except:
                print ('error')
            td.append(thread)
            no += 1
    if td != []:
        start(td)

    #print (datetime.datetime.now())
