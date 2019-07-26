'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：
1、有右子树的，那么下个结点就是右子树最左边的点；
2、没有右子树的，也可以分成两类，a)是父节点左孩子，那么父节点就是下一个节点 ； 
b)是父节点的右孩子找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。
如果没有，那么他就是尾节点。
'''
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp 
            pNode = tmp 







