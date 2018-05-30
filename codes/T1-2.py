# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 17:14:52
"""

# T1-2 由两个栈组成的队列
# 编写一个类，用两个栈实现一个队列，支持队列的基本操作
# add、poll、peek

# add:队尾添加，poll：队头删除，peek：返回队头
# 用两个栈保存队列中的数据，栈1用于存push的数据
# 栈2用于pop数据。如果栈2为空，则将栈1的元素全部
# 取出来放到栈2（先进后出 + 先进后出 => 先进先出）

class Queue():
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def add(self, x):
        self.Stack1.append(x)
    
    def poll(self):
        if(self.Stack2 != []):
            return self.Stack2.pop()
        else:       # 如果stack2空了，则把stack1里面的数据全部加入到stack1
            while(self.Stack1 != []):
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()
    
    def peek(self):
        if(self.Stack2 != []):
            return self.Stack2[-1]
        else:       # 如果stack2空了，则把stack1里面的数据全部加入到stack1
            while(self.Stack1 != []):   
                self.Stack2.append(self.Stack1.pop())
            if(self.Stack2 != []):
                return self.Stack2[-1]

if __name__ == "__main__":
    s = Queue()
    s.add(1)
    print(s.peek())
    s.add(3)
    print(s.peek())
    s.add(2)
    print(s.peek())
    print(s.poll())
    print(s.poll())
    print(s.poll())