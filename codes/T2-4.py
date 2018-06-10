# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-10 15:48:18
"""

# T2-4 反转单向与双向链表
# 分别实现反转单向链表和反转双向链表的函数
# 要求时间复杂度为O(N)，空间复杂度为O(1)

# 思路：对于单向链表的反转，首先链表长度至少为2，否则不需要反转
# 如果长度大于等于2，则可以使用三指针法，来进行反转。
# 如果是双向链表，只是多一步指针操作

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

def reverseList(head):
    pre = None
    nex = None
    
    while(head != None):
        nex = head.next
        head.next = pre
        #如果是双向链表，加一步操作即可head.last = nex
        pre = head
        head = nex
    
    return pre

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

head = reverseList(head)
printList(head)
