# 代码结构

[TOC]

## 核心模块

- [Book.py](../Book.py)

  - Book (预约相关)

    - *index(first, second=-1)*

      定位配置文件中的账号密码

    - login(self)

      CAS登录

    - prepare(self, room, seat, date)

      预约准备

    - book(self)

      预约

- [General.py](../General.py)

  - General

    通用的方法。

- Maintain.py

  - detect()

    检测僵尸账号是否正常

- Manage.py  (不对外公开)

  - Manage

    - login(self)
    - query_info(self, action, student_id='', page=1)
    - del_renege(self, student_id)
    - del_book(self, sid, date_delta)
    - get_book_time(self, href)

  - Crawl

    爬取数据

    - *crawl_user()*
    - *crawl_book()*

  - rm_space(string)

## 功能模块



------

[联系作者](mailto:code@defjia.top)