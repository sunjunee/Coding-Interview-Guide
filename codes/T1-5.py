# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-02 20:05:09
"""

# T1-5 用一个栈实现另一个栈的排序
# 一个栈中元素的类型为整型，现在想将该栈从顶到底按照从小到大的顺序进行排序
# 只许申请一个栈，除此之外可以申请新的变量，但是不能申请额外的数据结构。

# 思路：维护栈2，从顶到底从小到大
# 对于栈1栈顶的元素a，出栈，如果a小于栈2栈顶元素，则直接入栈2
# 否则将栈2小于a的元素依次出栈并压入栈1，
# 循环知道栈1为空

def SortingStack(stack):
    if(len(stack) == 0):    return None

    stack2 = []
    while(stack != []):
        a = stack.pop()
        if(stack2 == [] or stack2[-1] >= a):
            stack2.append(a)
        else:
            while(stack2 != [] and stack2[-1] < a):
                stack.append(stack2.pop())
            stack2.append(a)
    return stack2
    
if __name__ == "__main__":
    print(SortingStack([5,3,1,6,7,2,4]))

