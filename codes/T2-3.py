# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-10 15:26:35
"""

#T2-3 删除链表的中间节点和a/b处的节点
#（1）给定链表的头部节点head，实现删除链表的中间节点的函数
#（2）给定链表的头结点head，整数a和b，实现删除位于a/b处节点的函数

# 如果删除中间节点，首先需要知道链表的长度，遍历得到
# 然后取其一半并四舍五入，得到要删除的节点是第k个，
# 删除之
# 如果删除a/b处的节点，和上面同理，得到要删除的节点是
# 第k个，删除之

import math

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

def deletNode(head, lens, k):
    if(k < 1 or k > lens):
        return head
    
    newHead = ListNode(0)
    newHead.next = head
    head = p = newHead
    
    for i in range(1, k):
        p = p.next
    
    p.next = p.next.next
    
    return head.next

def delCenterNode(head):
    if(head == None):   return
    
    lens = 0
    p = head
    while(p):
        p = p.next
        lens += 1
    
    k = round(lens / 2 + 0.1)   #python无法实现真正的四舍五入
    
    return deletNode(head, lens, k)
    

def delABNode(head, a, b):
    if(head == None):   return
    
    lens = 0
    p = head
    while(p):
        p = p.next
        lens += 1
    
    k = round(math.ceil(a / b * lens))   #python无法实现真正的四舍五入
    
    return deletNode(head, lens, k)
    

def printList(head):
    while(head):
        print(head.x, " -> ", end='')
        head = head.next
    print("")

head = p = ListNode(0)
p.next = ListNode(1);   p = p.next
p.next = ListNode(2);   p = p.next
p.next = ListNode(3);   p = p.next
p.next = ListNode(4);   p = p.next
p.next = ListNode(5);   p = p.next
printList(head)

head = delCenterNode(head)
printList(head)

head = delABNode(head, 5, 6)
printList(head)