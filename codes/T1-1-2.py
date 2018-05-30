# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 16:37:41
"""

# T1-1-2 设计一个有getMax功能的栈
# 要求pop、push、getMax操作的时间复杂度都是O(1)
# 设计栈的类型可以使用线程的栈结构

# 设计一个栈存储数据，另外一个栈保存当前的最大值序列
# 每次入栈时，入栈的数字需要与最大值栈内的元素比较
# 如果小于栈顶元素，则跳过，如果大于等于则入栈

class Stack():
    def __init__(self):
        self.DataStack = []     #存储数据的栈
        self.MaxStack = []      #存储当前最大值序列的栈，栈顶元素是当前栈的最大值

    def getMax(self):
        if(self.MaxStack != []):
            return self.MaxStack[-1]    #返回最大值
    
    def pop(self):
        if(self.DataStack != []):       
            res = self.DataStack.pop()  #数据栈的栈顶元素返回
            if(self.MaxStack[-1] == res):   #如果最大值栈的栈顶与返回元素相等
                self.MaxStack.pop()     #最大值栈的栈顶出栈
            return res
    
    def push(self, x):
        self.DataStack.append(x)
        if(self.MaxStack == [] or x >= self.MaxStack[-1]):  #最大值栈为空，或者x不小于栈顶元素，则更新最小值
            self.MaxStack.append(x)
        
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    print(s.getMax())
    s.push(2)
    print(s.getMax())
    s.push(1)
    print(s.getMax())
    s.push(0)
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())
    s.pop()
    print(s.getMax())