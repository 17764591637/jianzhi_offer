'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）
形成树的一条路径，最长路径的长度为树的深度。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归
# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         if not pRoot:
#             return 0
#         nleft = self.TreeDepth(pRoot.left)
#         nright = self.TreeDepth(pRoot.right)

#         return max(nleft+1,nright+1)

#非递归
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        currentStack = [pRoot]
        deepth = 0
        while currentStack:
            tmp = []
            for node in currentStack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            currentStack = tmp 
            deepth += 1 

        return deepth