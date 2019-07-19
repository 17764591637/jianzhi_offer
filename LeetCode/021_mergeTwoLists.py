#Definition for singly-linked list.
'''将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1 
                l1 = l1.next
            else:
                head.next = l2 
                l2 = l2.next
            
            head = head.next

        if l1:
            head.next = l1 
        if l2:
            head.next = l2 
        
        return dummy.next


        