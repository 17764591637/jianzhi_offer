'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：分两步：

第一步：确定链表是否有环。定义快慢指针：pFast,pSlow;pFast每次走两步，pSlow每次走一步，
进行遍历，如果两个指针相遇，即pFast=pSlow，则链表有环，如果pFast达到链表尾部（pFast->next=nullptr）
两个指针都没有相遇，则链表没有环。

第二步：找到环的入口。首先确定环中节点的个数n，从第一步快慢指针相遇的节点出发，一边继续向前移动一边计数，
当再次回到这个节点时，就可以得到环中节点个数n。然后定义连个指针p1,p2,p1先向前移动n步，
p1和p2以相同的速度想想移动，当p2==p1时，即为入口节点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#方法一
'''
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if self.judge_loop(pHead):
            if not pHead:
                return None 
            slow_cur = pHead
            fast_cur = pHead

            while slow_cur.next and fast_cur.next.next:
                slow_cur = slow_cur.next
                fast_cur = fast_cur.next.next
                #当两个指针相遇，说明有环，循环结束
                if slow_cur == fast_cur:
                    break
            #快指针停留在相遇处，慢指针回到起点
            if not fast_cur or not fast_cur.next:
                return None 
            slow_cur = pHead
            #两个指针每次向前移动1，当每次相遇时，相遇点即为入环节点
            while slow_cur != fast_cur:
                slow_cur = slow_cur.next
                fast_cur = fast_cur.next
            return slow_cur
        else:
            return None

    def judge_loop(self,node_list):
        p1 = p2 = node_list
        while p2.next and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True 
        return False
    
if __name__ == "__main__":
    LList = ListNode(0)
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)
    LList.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p2
    s = Solution()
    print (s.EntryNodeOfLoop(LList).val)
'''
#方法二
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        node_list = []
        p = pHead
        while p:
            if p in node_list:
                return p 
            else:
                node_list.append(p)
            p = p.next
