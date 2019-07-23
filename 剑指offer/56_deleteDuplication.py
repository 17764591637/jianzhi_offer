'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        cur = pHead
        r = ListNode(-1)
        res = r
        while cur != None:
            if cur.next != None and cur.val == cur.next.val:
                while cur.next != None and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                r.next = cur
            else:
                r.next = cur 
                r = cur 
                cur = cur.next

        return res.next

if __name__ == "__main__":
    LList = ListNode(0)
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(3)
    p5 = ListNode(4)
    p6 = ListNode(4)
    p7 = ListNode(5)
    LList.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p6
    p6.next = p7
    s = Solution()
    r = s.deleteDuplication(LList)
