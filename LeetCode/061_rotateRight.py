'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def rotateRight(self, head, k):
#         if not head:
#             return head
#         l = 1
#         p = head
#         #计算链表的长度
#         while p.next:
#             l += 1
#             p = p.next
#         k = k%l
#         if k == 0:
#             return head

#         k = l - k%l - 1
#         pp = head
#         while k > 0:
#             pp = pp.next
#             k -= 1 
#         newHead = pp.next
#         pp.next = None
#         p.next = head

#         return newHead
#方法二：先连成环，在断开
class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        start,end,len = head,None,0
        while head:
            end = head
            head = head.next
            len += 1 
        end.next = start
        pos = len - k % len 
        while pos>1:
            start = start.next
            pos -= 1 
        ret = start.next
        start.next = None 
    
        return ret

        