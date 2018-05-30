# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-05-30 21:15:25
"""

# T1-3 如何仅用递归函数和栈操作逆序一个栈
# 实现栈中的元素逆序，但是只能用递归函数来实现，
# 不能使用其他数据结构

# 处理的流程并不是很直观 ，但是容易想到：
# 仅用一个函数的递归是不行的，因为栈内元素依次出栈
# 之后，递归完再依次入栈，顺序不变。
# 具体分为三个步骤：1、获取栈底元素，2、递归 3、压入栈
# 对于取出栈底元素，也需要递归调用，将数据出栈，然后压入栈

def TranVerse(stack):
    if(stack == []):
        return
    tail = getTail(stack)   #从栈中取出了栈底元素
    TranVerse(stack)        #递归调用
    stack.append(tail)      #将栈底元素放入栈

def getTail(stack):
    if(len(stack) == 1):    #如果栈内只有一个元素了，那么就是栈底元素
        return stack.pop()
    item = stack.pop()
    tail = getTail(stack)   #递归调用
    stack.append(item)
    
    return tail             #返回栈底元素

if __name__ == "__main__":
    stack = [1,2,3,4,5]
    TranVerse(stack)
    print(stack)
    