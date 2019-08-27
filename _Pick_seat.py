from Book import Book
from Query import Query
import time
from datetime import datetime
from General import General
from Notify import Music, Massage_box, Output


if __name__ == '__main__':
    cfg = General.get_config()[0]
    output = Output()
    music = Music()
    message_box = Massage_box('')

    search = {'X':0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
    all = range(1,10)
    target_users = cfg.get('_Pick_seat', 'target_users').split(',')
    target_rooms = cfg.get('_Pick_seat', 'target_rooms').split(',')
    ori_seat = [(x.split('-')[0],search[x.split('-')[1]]) for x in target_rooms]
    target_seat = ori_seat.copy()
    for elem in ori_seat:
        if elem[1] == 0:
            for i in all:
                target_seat.append((elem[0],i))
    target_seat = list(set([x for x in target_seat if x[1]!= 0]))
                
    date = cfg.getint('_Pick_seat', 'date')
    sleep_second = cfg.getint('_Pick_seat', 'interval')

    use_music = cfg.getboolean('Notify', 'use_music')
    use_messagebox = cfg.getboolean('Notify', 'use_messagebox')
    cur = 0
    while len(target_users) and len(target_seat):
        try:
            # 获取可用座位信息
            query = []
            target_floor = set(x[0] for x in target_seat)
            for floor in target_floor:
                q = Query(date, floor)
                query += q.get_list()
            query = set(query)
            cur += 1

            # 若有可用座位
            if len(query) != 0:
                # 判断是否为所指定座位
                del_sid = []
                for sid in range(len(target_seat)):
                    if target_seat[sid] in query:
                        seat = target_seat[sid]
                        room_id = seat[0]
                        seat_id = seat[1]
                        text = format('%s-%s次车有余票，正在尝试下单，下单用户%s' % (room_id, seat_id, target_users[0]) )
                        output.continuous_output(text)

                        account = Book(target_users[0])
                        account.prepare(room_id, seat_id, date)
                        account.book()
                        
                        text = format('%s-%s次车，下单成功，下单用户%s' % (room_id, seat_id, target_users[0]) )
                        if use_music:
                            music.play_audio_async()
                        if use_messagebox:
                            message_box.text = text
                            message_box.show_messagebox_async()
                        output.continuous_output(text)

                        # 删除该用户&预约座位&查询
                        del target_users[0]
                        del_sid.append(sid)
                        query.remove(seat)
                        if not target_users:
                            cur = -1
                            text = format('提醒：已无可用用户,即将退出！')
                            output.continuous_output(text)
                            target_seat.clear()
                            break
                # 更新剩余指定车次列表
                target_seat = [target_seat[x] for x in range(len(target_seat)) if x not in del_sid ]
                if len(target_seat) != 0:
                    text = format('第%d次查询，仍有车次未预约成功！时间%s...' % (cur, str(datetime.now())[:-7]))
                    if len(query) !=0:
                        text += format('\t*提醒：在指定范围之外有空余车次可用*')
                    output.continuous_output(text)
                elif len(target_seat) == 0:
                    text = format('恭喜您所有指定车次均已预约成功！')
                    output.continuous_output(text)
            else:
                text = format('第%d次查询，所有列车均无余票，时间%s...' % (cur, str(datetime.now())[:-7]))
                output.continuous_output(text)
            time.sleep(sleep_second)
        except Exception as e:
            output.continuous_output(repr(e))
