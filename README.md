# LIT后花园观景台预约系统后台

​	本系统由Defjia从2017.11开始开发，经过数次迭代和一次重构，这里是重构后的代码。

[TOC]

## 文件结构
 - Core Codes
    - Book.py
        - Book  (预约相关)
            - login(self)
            - prepare(self, room, seat, date)
            - book(self)
    - General.py
        - General
            通用的方法。
    - Maintain.py
        - 
    - Manage.py  (包含后台操作，不对外公开)
        - Manage
            - login(self)
            - query_info(self, action, student_id='', page=1)
            - 