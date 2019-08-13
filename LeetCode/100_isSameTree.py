'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        root1 = p
        root2 = q
        if root1 is None and root2 is None:
            return True
        elif root1 and root2:
            return root1.val==root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        else:
            return False