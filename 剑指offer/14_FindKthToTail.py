'''
输入一个链表，输出该链表中倒数第k个结点。
'''
class Solution:
    def FindKthToTail(self, head, k):
        res = []
        while head:
            res.append(head)
            head = head.next
        if k>len(res) or k<1:
            return
        return res[-k]