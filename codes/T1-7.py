# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-02 21:11:17
"""

# T1-7 生成窗口的最大值
# 有一个整型数组arr和一个大小为w的窗口从数组的最右边滑到最右边
# 窗口每次向右边滑动一个位置
# 如果数组长度为n，窗口长度为w，那么移动产生n-w+1个窗口的最大值

# 滑动窗口的问题，类似于求队列的最大值，用另一个队列来保存最大值(index)

def getMaxValInWindow(arr, w):
    lens = len(arr)
    if(lens < w):   return None
    
    resu = []
    maxQueue = [arr[0]]
    for i in range(1, lens):
        # 如果队头元素已经在window外，需要去掉（不是当前窗口的最大值了）
        if(i - maxQueue[0] == w):
            del maxQueue[0]

        # 在最大值队列中去除小于当前值arr[i]的值，并将arr[i]入队列
        while(maxQueue != [] and arr[maxQueue[-1]] < arr[i]):
            del maxQueue[-1]
        maxQueue.append(i)
        
        # 计算当前窗口的最大值
        if(i >= w - 1):
            resu.append(arr[maxQueue[0]])
    return resu

if __name__ == "__main__":
    print(getMaxValInWindow([4,3,5,4,3,3,6,7], 3))
        
        