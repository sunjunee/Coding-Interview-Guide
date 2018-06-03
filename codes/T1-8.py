# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-02 21:28:28
"""

# T1-8 构造数组的MaxTree
# 一个数组的MaxTree定义：
# · 数组必须没有重复的元素
# · MaxTree是一颗二叉树，数组的每一个值对应一个二叉树节点
# · 包括MaxTree树在内且在其中的每一颗子树上，值最大的节点都是树的头
# 给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree的函数，
# 要求如果数组长度为N，则时间复杂度为O(N),额外的空间复杂度为O(N)

# 完全按书上的思路来的，这一题没有什么标准答案，感觉很搞笑啊
# 用两个dict来保存节点之间的关系，分别是节点左边比它大的第一个节点
# 以及节点右边第一个比它大的节点。(由于python dict的限制，我们只
# 在dict里面保存节点的index，节点预先构建，并存在数组中)

class Node():
    def __init__(self, x):
        self.left = None
        self.right = None
        self.x = x
  
def addNodeToDict(lDcit, stack):
    i = stack.pop()
    if(len(stack) == 0):
        lDcit[i] = None
    else:
        lDcit[i] = stack[-1]
        
def getMaxTree(nums):
    nodes = [Node(n) for n in nums]
    
    stack = []  # 用于存储当前的最大值栈
    #计算每个节点左边第一个大节点和右边第一个大节点
    lDict, rDict = {}, {}   # 实际上存的是父节点的index
    for i, node in enumerate(nodes):
        while(len(stack) > 0 and nodes[stack[-1]].x < node.x):
            addNodeToDict(lDict, stack)
        stack.append(i)
    
    while(stack != []):
        addNodeToDict(lDict, stack)
    
    for i, node in enumerate(nodes[::-1]):
        i = len(node) - i - 1
        while(len(stack) > 0 and nodes[stack[-1]].x < node.x):
            addNodeToDict(rDict, stack)
        stack.append(i)
    
    while(stack != []):
        addNodeToDict(rDict, stack)  
    
    root = None
    #构建树:把节点连接到父节点上，看父节点的左右是否有节点了
    for i, node in enumerate(nodes):
        left, right = lDict.get(i), rDict.get(i)
        if(left == None and right == None):
            root = node
        elif(left == None):
            parentNode = nodes[right]
            if(parentNode.left != None):
                parentNode.left = node
            else:
                parentNode.right = node
        elif(right == None):
            parentNode = nodes[left]
            if(parentNode.left != None):
                parentNode.left = node
            else:
                parentNode.right = node
        else:
            parentNode = nodes[right] if nodes[left].x > nodes[right].x else nodes[right]

    return root