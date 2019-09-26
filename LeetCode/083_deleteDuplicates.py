'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def deleteDuplicates(self, head):
#         res = ListNode(0)
#         res.next = head
#         cur = res
#         while cur.next:
#             begin = cur.next
#             if begin.next != None and begin.val == begin.next.val:
#                 end = begin.next
#                 while end.next and end.val == end.next.val:
#                     end = end.next
#                 cur.next = end
#             else:
#                 cur = cur.next

#         return res.next

class Solution:
    def deleteDuplicates(self, head):
        ans = head
        while head != None:
            if head.next != None and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
                
        return ans