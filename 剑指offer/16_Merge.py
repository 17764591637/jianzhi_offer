'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        mergeHead = ListNode(-1)
        p = mergeHead
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
            else:
                mergeHead.next = pHead1
                pHead1 = pHead1.next
            mergeHead = mergeHead.next
            
        if pHead1:
            mergeHead.next = pHead1
        if pHead2:
            mergeHead.next = pHead2
        
        return p.next
            