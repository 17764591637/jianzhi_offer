                            '''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

思路：
1.找终止条件：本题终止条件很明显，当递归到链表为空或者链表只剩一个元素的时候，没得交换了，自然就终止了。
2.找返回值：返回给上一层递归的值应该是已经交换完成后的子链表。
3.单次的过程：因为递归是重复做一样的事情，所以从宏观上考虑，只用考虑某一步是怎么完成的。
'''                                                                                                                       
      
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        tmp = head.next 
        head.next = self.swapPairs(head.next.next) 
        tmp.next = head 

        return tmp

# class Solution:
#     def swapPairs(self, head):
#         def reverseList(head,k):
#             pre = None
#             cur = head
#             while cur and k > 0:
#                 tmp = cur.next
#                 cur.next = pre 
#                 pre = cur 
#                 cur = tmp 
#                 k -= 1
#             head.next = cur 
#             return cur,pre
        
#         if not head or not head.next:
#             return head
            
#         ret = head.next
#         p = head
#         pre = None
#         while p:
#             next,newHead = reverseList(p,2)
#             if pre:
#                 pre.next = newHead
#             pre = p 
#             p = next
#         return ret