# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 09:24:13
"""

# T1-1 设计一个有getMin功能的栈
# 要求pop、push、getMin操作的时间复杂度都是O(1)
# 设计栈的类型可以使用线程的栈结构

# 设计一个栈存储数据，另外一个栈保存当前的最小值序列
# 每次入栈时，入栈的数字需要与最小值栈内的元素比较
# 如果大于栈顶元素，则跳过，如果小于等于则入栈

class Stack():
    def __init__(self):
        self.DataStack = []     #存储数据的栈
        self.MinStack = []      #存储当前最小值序列的栈，栈顶元素是当前栈的最小值

    def getMin(self):
        if(self.MinStack != []):
            return self.MinStack[-1]    #返回最小值

    def pop(self):
        if(self.DataStack != []):
            res = self.DataStack.pop()  #数据栈的栈顶元素返回
            if(self.MinStack[-1] == res):   #如果最小值栈的栈顶与返回元素相等
                self.MinStack.pop()     #最小值栈的栈顶出栈
            return res

    def push(self, x):
        self.DataStack.append(x)
        if(self.MinStack == [] or x <= self.MinStack[-1]):  #最小值栈为空，或者x不大于栈顶元素，则更新最小值
            self.MinStack.append(x)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    print(s.getMin())
    s.push(2)
    print(s.getMin())
    s.push(1)
    print(s.getMin())
    s.push(0)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.pop()
    print(s.getMin())
