'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        res = ListNode(-1)
        res.next = head
        node = res
        for _ in range(m-1):
            node = node.next
        split_node = node.next
        node.next = self.reverse_k_times(split_node,n-m)

        return res.next
    
    def reverse_k_times(self,head,k):
        cur = head
        next_node = cur.next
        for _ in range(k):
            temp = next_node.next
            next_node.next = cur
            cur = next_node
            next_node = temp
        head.next = next_node

        return cur 