# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-09 20:45:31
"""

# T2-1 打印两个有序链表的公共部分
# 给定两个有序链表的头指针head1和head2，
# 打印两个链表的公共部分

# 类似于找一个带环链表的入口位置
# 首先从两个入口分别遍历两个链表，计算长度及差值d
# 然后让长的先走d步，然后一起走，知道指针指向相同。

class ListNode():
    def __init__(self, x):
        self.x = x
        self.next = None

def getCommonNode(head1, head2):
    p1, p2 = head1, head2
    l1, l2 = 0, 0
    while(p1 != None):
        l1 += 1
        p1 = p1.next
    while(p2 != None):
        l2 += 1
        p2 = p2.next
    
    p1, p2 = head1, head2
    if(l2 > l1):
        for i in range(l2 - l1):
            p2 = p2.next
    else:
        for i in range(l1 - l2):
            p1 = p1.next
    
    while(p1 != p2):
        p1, p2 = p1.next, p2.next
    
    return p1
    
head1 = p = ListNode(0)
p.next = ListNode(1);   p = p.next
p.next = ListNode(2);   p = p.next
p.next = ListNode(3);   p = p.next;     c = p;

head2 = p = ListNode(2)
p.next = c; p = p.next

p.next = ListNode(4);

print(getCommonNode(head1, head2).x)