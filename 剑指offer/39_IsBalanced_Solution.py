'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
思路：左右子树间的深度差不超过1
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, root):
        if not root:
            return True
        if not self.IsBalanced_Solution(root.left) or not self.IsBalanced_Solution(root.right):
            return False
        
        left_d = self.TreeDepth(root.left)
        right_d = self.TreeDepth(root.right)
        if abs(left_d-right_d) < 2:
            return True
            
        return False
     
    def TreeDepth(self,pNode):
        if not pNode:
            return 0
        nleft = self.TreeDepth(pNode.left)
        nright = self.TreeDepth(pNode.right)

        return max(nleft+1,nright+1)

