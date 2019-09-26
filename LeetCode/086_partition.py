'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        min_list = ListNode(0)
        max_list = ListNode(0)
        h1 = min_list
        h2 = max_list
        cur = head
        while cur:
            if cur.val < x:
                min_list.next = cur
                min_list = min_list.next
            else:
                max_list.next = cur
                max_list = max_list.next
            cur = cur.next
        if h1.next == None:
            return h2.next
        elif h2.next == None:
            return h1.next
        else:
            max_list.next = None
            min_list.next = h2.next
            return h1.next




        