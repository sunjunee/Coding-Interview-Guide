# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 16:42:47
"""

# T1-1-3 设计一个有getMin功能的队列
# 要求pop、push、getMin操作的时间复杂度都是O(1)
# 设计队列的类型可以使用线程的队列结构

# 设计一个队列存储数据，另外一个队列保存当前的最小值序列
# 每次入队列时，入队的数字需要与最小值队列内的元素依次比较
# 如果大于等于队尾元素，则入队列，如果小于队尾元素，则队尾
# 元素移出队列

class Queue():
    def __init__(self):
        self.DataQueue = []
        self.MinQueue = []
    
    def getMin(self):
        if(self.MinQueue != []):
            return self.MinQueue[0]
    
    def pop(self):
        if(self.DataQueue != []):
            res = self.DataQueue[0]
            del self.DataQueue[0]
            if(self.MinQueue[0] == res):
                del self.MinQueue[0]

    def push(self, x):
        self.DataQueue.append(x)
        while(self.MinQueue != [] and self.MinQueue[-1] > x):
            del self.MinQueue[-1]
        self.MinQueue.append(x)
    
if __name__ == "__main__":
    s = Queue()
    s.push(1)
    print(s.getMin())
    s.push(3)
    print(s.getMin())
    s.push(1)
    print(s.getMin())
    s.push(2)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())