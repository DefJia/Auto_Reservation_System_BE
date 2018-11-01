# 使用说明

[TOC]

## 简介

本使用说明旨在帮助非开发者的Windows用户方便快速地使用本系统预约座位。

## 初始化

### 环境要求

- Python3 & pip3
- GitHub Desktop / Git
- 文本编辑器

### 步骤

1. Clone项目代码到本地

2. 命令行切换到项目根目录下，运行命令：

   `pip3 install -r  requirements.txt`

3. 复制.config.example.ini为.config.ini，并按照说明添加相关个性化信息。

## 使用方法

所有以**单下划线**命名的文件为可用功能，一个文件对应一个功能，需要提前在配置文件中修改对应参数，然后才可以运行，否则会报错。

### 自动预约 

按照.config.example.ini的示例和注释，修改或填写.config.ini中_Auto_book和Time（不建议修改）下的参数；同时还要确保Account中至少有一个账号信息。

### 模拟预约

按照.config.example.ini的示例和注释，修改或填写.config.ini中_Book_seat下的参数；同时还要确保Account中有对应的账号信息。

### 捡漏座位

### 删除违约（高级功能）

### 预约过户（高级功能）

## 代码更新

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

[联系作者](mailto:code.defjia.top)