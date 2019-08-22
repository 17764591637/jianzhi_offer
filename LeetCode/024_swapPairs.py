'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def swapPairs(self, head):
#         if not head or head.next:
#             return head
        
#         _next = head.next
#         head.next = self.swapPairs(_next.next)
#         _next.next = head

#         return _next

class Solution:
    def swapPairs(self, head):
        def reverseList(head,k):
            pre = None
            cur = head
            while cur and k > 0:
                tmp = cur.next
                cur.next = pre 
                pre = cur 
                cur = tmp 
                k -= 1
            head.next = cur 
            return cur,pre
        
        if not head or not head.next:
            return head
            
        ret = head.next
        p = head
        pre = None
        while p:
            next,newHead = reverseList(p,2)
            if pre:
                pre.next = newHead
            pre = p 
            p = next
        return ret