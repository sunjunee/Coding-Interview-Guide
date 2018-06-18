# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 17:11:45
"""


# T1-1-4 设计一个有getMax功能的队列
# 要求pop、push、getMax操作的时间复杂度都是O(1)
# 设计队列的类型可以使用线程的队列结构

# 设计一个队列存储数据，另外一个队列保存当前的最大值序列
# 每次入队列时，入队的数字需要与最大值队列内的元素依次比较
# 如果小于等于队尾元素，则入队列，如果大于队尾元素，则队尾
# 元素移出队列

class Queue():
    def __init__(self):
        self.DataQueue = []
        self.MaxQueue = []

    def getMax(self):
        if(self.MaxQueue != []):
            return self.MaxQueue[0]

    def pop(self):
        if(self.DataQueue != []):
            res = self.DataQueue[0]
            del self.DataQueue[0]
            if(self.MaxQueue[0] == res):
                del self.MaxQueue[0]

    def push(self, x):
        self.DataQueue.append(x)
        while(self.MaxQueue != [] and self.MaxQueue[-1] < x):
            del self.MaxQueue[-1]
        self.MaxQueue.append(x)

if __name__ == "__main__":
    s = Queue()
    s.push(1)
    print(s.getMax())
    s.push(3)
    print(s.getMax())
    s.push(1)
    print(s.getMax())
    s.push(2)
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
