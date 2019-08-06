'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
归并排序

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def sortList(self, head):
#         if head is None or head.next is None:
#             return head
#         mid = self.get_mid(head)
#         l = head
#         r = mid.next
#         mid.next = None

#         return self.merge(self.sortList(l),self.sortList(r))
    
#     def merge(self,p,q):
#         tmp = ListNode(0)
#         h = tmp 
#         while p and q:
#             if p.val < q.val:
#                 h.next = q
#                 p = p.next
#             else:
#                 h.next = q
#                 q = q.next
#             h = h.next
#         if p:
#             h.next = p 
#         if q:
#             h.next = q 
        
#         return tmp.next

#     def get_mid(self,node):
#         if node is None:

#             return node
#         fast = slow = node 
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         return slow

class Solution:
    def sortList(self, head):
        if not head or not head.next:  # 如果无节点或只有一个节点
            return head
        elif not head.next.next:  # 如果刚好两个结点
            if head.next.val < head.val:  # 更正顺序
                head.next.next = head
                head = head.next
                head.next.next = None
            return head

        slow, fast = head, head  # 快慢指针找中点,slow为找到的中点
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 截断并分别递归
        head2 = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)

        # 合并
        if not l1 or not l2:
            return l1 or l2
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next