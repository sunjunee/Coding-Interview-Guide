# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 21:46:32
"""

# T1-4 猫狗队列
# 实现一种猫狗队列的结构，要求如下：
# · 用户可以调用add方法将cat类或者dog类放入队列中；
# · 用户可以调用pollAll方法，将队列中所有的实例按照队列的先后顺序依次弹出；
# · 用户可以调用pollDog方法，将队列中dog类的实例按照进队的先后顺序依次弹出；
# · 用户可以调用pollCat方法，将队列中cat类的实例按照进队的先后顺序依次弹出；
# · 用户可以调用isEmpty方法，检查队列中是否有cat或者dog的实例；