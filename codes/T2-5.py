# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-10 16:05:10
"""

# T2-5 反转部分单向链表
# 给定一个单向链表的头结点head，以及两个整数from和to，在单向链表上把
# 第from个节点到第to个节点进行反转。

# 思路：找到from-1、to+1两个节点的指针，然后对from、to进行reverse
# 然后拼接即可

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

def reversePartOfList(head, a, b):
    newHead = ListNode(0)
    newHead.next = head
    head = newHead    
    
    pre = pre1 = pre2 = head
    p = p1 = p2 = head
    count = 0
    while(p):
        p = p.next
        count += 1
        if(count == a):
            pre1 = pre
            p1 = p
            pre1.next = None
        if(count == b):
            pre2 = p
            p2 = p.next
            pre2.next = None
            
        pre = p
    
    if(a > b or a < 1 or b > count):
        return head.next
        
    p1 = reverseList(p1)    #复用了前面的功能
    pre2 = p1
    while(pre2.next):
        pre2 = pre2.next
    
    pre1.next = p1
    pre2.next = p2

    return head.next

head = p = ListNode(0)
p.next = ListNode(1);   p = p.next
p.next = ListNode(2);   p = p.next
p.next = ListNode(3);   p = p.next
p.next = ListNode(4);   p = p.next
p.next = ListNode(5);   p = p.next
printList(head)

head = reversePartOfList(head, 1, 6)
printList(head)
    