'''
输入两个链表，找出它们的第一个公共结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list_1 = []
        list_2 = []
        while pHead1:
            list_1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            list_2.append(pHead2)
            pHead2 = pHead2.next
            
        res = None
        for i in range(min(len(list_1),len(list_2))):
            if list_1[-1] == list_2[-1]:
                tmp = list_1[-1]
                res = tmp
                list_1.pop()
                list_2.pop()
            else:
                break
                
        return res
