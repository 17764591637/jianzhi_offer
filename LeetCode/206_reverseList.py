'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        # write code here
        if  not head or not head.next:
            return head
        p_before = None 
        pNode = head
        while pNode != None:
            pNext = pNode.next
            pNode.next = p_before
            p_before = pNode
            pNode = pNext
            
        return p_before