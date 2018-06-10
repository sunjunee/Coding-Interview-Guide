# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-10 10:56:27
"""

# T2-2 在单链表和双链表中删除倒数第k个节点

# 思路：分两步-（1）遍历链表得到链表长度l，
#            （2）倒数第k个，即正数第l-k+1个
#            （3）删除之即可。

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

def deleteNode(head, k):
    lens = 0
    
    p = head
    while(p):
        lens += 1
        p = p.next
    
    if(k < 1 or k > lens):
        return head
    
    newHead = ListNode(0)
    newHead.next = head
    p = head = newHead
    for i in range(1, lens - k + 1):
        p = p.next
    
    #删除
    p.next = p.next.next
    
    return head.next

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

head = deleteNode(head, 4)
printList(head)