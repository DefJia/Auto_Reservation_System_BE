# 使用说明

[TOC]

## 简介

本使用说明旨在帮助非开发者的Windows用户方便快速地使用本系统预约座位。

## 初始化

### 环境要求

- [Python3](https://www.python.org/downloads/)

- [pip3](https://pypi.org/project/pip/)（一般安装Python时自带）

  - [安装帮助 - 官方文档](https://pip-cn.readthedocs.io/en/latest/installing.html)
  - [安装帮助 - 菜鸟教程](http://www.runoob.com/w3cnote/python-pip-install-usage.html)

- [GitHub Desktop(功能强大的图形化界面)](https://desktop.github.com/) / [Git(可选命令行或简洁的图形化界面)](https://git-scm.com/downloads)

- 文本编辑器（主要用来编辑配置文件）

  记事本即可，也可使用[Sublime](https://www.sublimetext.com/3)、[Notepad++](https://notepad-plus-plus.org/download/v7.5.9.html)等工具。

- Python IDE（可选）

  - [Python IDE推荐 - 菜鸟教程](http://www.runoob.com/python/python-ide.html)

- Markdown软件（可选）

  主要用来在本地查看文档

  - [Typora](https://typora.io/#windows)

### 步骤

1. Clone项目代码到本地

   - 使用GitHub Desktop

     - 已有GitHub账号

       1. 在项目主页点击右上角Fork按钮，将项目Fork到个人主页

       （若不做此步骤，则可直接当做没有GitHub账号操作）

       2. 在GitHub Desktop上登录个人账户
       3. 依次点击File - Clone repository - GitHub.com - YourUsername/Auto_Reservation_System_BE - Clone

     - 没有GitHub账号

       1. 在GitHub Desktop中依次点击File - Clone repository - URL

       2. 在Repository URL一栏中输入

          `https://github.com/DefJia/Auto_Reservation_System_BE.git`

       3. 选择路径并点击Clone

   - 使用Git

     - 使用命令行（Git Bash）

       - 在文件管理器中切换到目标文件夹，在空白处点击右键，打开Git Bash
       - `git clone https://github.com/DefJia/Auto_Reservation_System_BE.git`

     - 使用图形化界面（Git GUI）

       - 在文件管理器的空白处点击右键，打开Git GUI

       - 点击Clone Existing Repository

       - 在Source Location中输入

         `https://github.com/DefJia/Auto_Reservation_System_BE.git`

       - 在Target Directory中选中目标文件夹

       - 点击Clone

2. 安装Python依赖库

   - 以管理员身份打开“[命令提示符](https://zh.wikihow.com/%E6%89%93%E5%BC%80Windows%E7%B3%BB%E7%BB%9F%E7%9A%84%E5%91%BD%E4%BB%A4%E6%8F%90%E7%A4%BA%E7%AC%A6)”

   - 切换到项目根目录下

     - `cd C:\xxx\path\xxx\`

   - 安装依赖

     - `pip3 install -r requirements.txt`

       若提示pip3不可执行，则尝试去掉“3”

3. 复制.config.example.ini为.config.ini，并按照文件内的说明在.config.ini中修改或添加相关个性化信息。

## 使用方法

所有以**单下划线**命名的文件为可用功能，一个文件对应一个功能，需要提前在配置文件中修改对应参数，然后才可以运行，否则会报错。

### 自动预约 

按照.config.example.ini的示例和注释，修改或填写.config.ini中_Auto_book和Time（不建议修改）下的参数；同时还要确保Account中至少有一个账号信息。

### 模拟预约

按照.config.example.ini的示例和注释，修改或填写.config.ini中_Book_seat下的参数；同时还要确保Account中有对应的账号信息。

### 捡漏座位

## 代码更新

### 使用GitHub Desktop

### 使用Git GUI

### 使用Git Bash

1. 在文件管理器中打开项目根目录，右键点击空白处，选中Git Bash并打开

2. 在命令框中运行

   `git pull`

3. 若报错，则运行

   `git reset --hard HEAD`

   后再回到2

## 注意事项

- 请勿擅自修改代码内容
- 尽量每次使用前进行代码更新

------

[联系作者](mailto:code@defjia.top)