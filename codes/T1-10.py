# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-09 19:49:21
"""

# T1-10 最大值减去最小值小于等于num的子数组的数量
# 返回子数组的个数

# 思路：考虑num中第j位以前，包含第j位的满足条件的子数组的
# 数量。已知第j-1位的子数组开始位置是i，判断从i到j的子数组
# 是否满足条件，满足则计算数量，不满足则i+1，直到等于j或者满足条件。
# 而子数组的最大值、最小值可以通过两个队列来实现

def getNumOfSubArray(nums, val):
    lens = len(nums)
    if(lens == 0):  return
    
    counts = 0
    maxQueue, minQueue = [], []
    
    j = 0    
    for i in range(lens):
        #更新最大最小值
        while((maxQueue != []) and (maxQueue[-1] < nums[i])):
            del maxQueue[-1]
        maxQueue.append(nums[i])
        while((minQueue != []) and (minQueue[-1] > nums[i])):
            del minQueue[-1]
        minQueue.append(nums[i])       
        
        #判断当前的i，j是否满足条件，不满足则j一直后移
        while((maxQueue[0] - minQueue[0]) > val and j < i):            
            if(maxQueue[0] == nums[j]):
                del maxQueue[0]
            if(minQueue[0] == nums[j]):
                del minQueue[0]
            j += 1
            
        counts += (i - j + 1)
        
    return counts

print(getNumOfSubArray([3,4,7,0,3,1,8   ], 3))
