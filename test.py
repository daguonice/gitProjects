#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @File : test.py
    @Author : 郭凯锋
    @Time : 2019/8/19 20:19
    @Software : PyCharm
    @Git-Hub : daguonice
    @e-mail : daguonice@163.com
    
"""

import random

# —————debug测试代码—————

b = random.randint(0, 500)
i = 0
while 1:
    a = input("请输入你猜的数：")
    i += 1
    if int(a) == b:
        print("猜对了！！")
        break
    elif int(a) > b:
        print("大了")
    else:
        print("小了")
print("您一共猜了" + str(i) + "次")


