'''
输入一个链表，反转链表后，输出新链表的表头。

思路：
step1:None
step2:1->None 
step3:2->1->None
... 
'''
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        p_before = None 
        pNode = pHead
        while pNode != None:
            pNext = pNode.next
            pNode.next = p_before
            p_before = pNode
            pNode = pNext
            
        return p_before