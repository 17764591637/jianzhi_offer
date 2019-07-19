# Definition for singly-linked list.
'''
首先声明一个虚拟结点，使删除归一化，不受 head 头部结点的干扰。
使用两枚指针 fast 指针 和 slow 指针，先让 fast 指针走 n + 1 步，再让 slow 指针和 fast 指针一起走。
在 fast 指针到达尾部时，slow 指针正好指向倒数第 n 个元素的前驱结点。
利用这个待删结点的前驱结点删除倒数第 n 个元素即可。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        cur = head
        pre = None 
        #先跑n步
        while cur and n>1:
            cur = cur.next
            n -= 1
        #节点总和不够n个时，直接返回头结点
        if n>1:
            return head
        
        #pre与cur同时向后跑
        while cur.next:
            if not pre:
                pre = head
            else:
                pre = pre.next
            cur = cur.next
        #删除的是头结点
        if not pre:
            return head.next
        else:
            pre.next = pre.next.next
            return head

