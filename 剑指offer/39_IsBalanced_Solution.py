'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        left_deepth = self.TreeDepth(pRoot.left)
        right_deepth = self.TreeDepth(pRoot.right)
        if abs(left_deepth-right_deepth) <= 1:
            return True
        return False

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        nleft = self.TreeDepth(pRoot.left)
        nright = self.TreeDepth(pRoot.right)

        return max(nleft+1,nright+1)

