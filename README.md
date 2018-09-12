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
   
 ## 版本记录
 
 ### 已修改内容
 - 修改文件结构。
 - Manage.del_reneges方法增加参数识别，方便切换删除账号的类别。
 - index方法修改为Book类的静态方法，可以通过拼音码(常用用户)、序号(僵尸账号)指定学号密码。
          
 ### 待修改内容
 
 #### 重要
 - 添加自动定时预约功能
 - 添加自动维护未签到座位功能
 
 #### 一般
 - 增加关注座位入馆提醒功能
 
 #### 不重要
 - 在config.ini中标注僵尸账号的可用性，以及修改相关方法。
 - 增加入馆时自动预约功能。