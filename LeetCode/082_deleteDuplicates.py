'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:
输入: 1->1->1->2->3
输出: 2->3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        res = ListNode(0)
        res.next = head
        cur = res
        while cur.next:
            begin = cur.next
            if begin.next != None and begin.val == begin.next.val:
                end = begin.next
                while end.next and end.val == end.next.val:
                    end = end.next
                cur.next = end.next
            else:
                cur = cur.next
        
        return res.next


