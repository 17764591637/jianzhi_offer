'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        elif root.left == None:
            return 1+self.minDepth(root.right)
        elif root.right == None:
            return 1+self.minDepth(root.left)
        else:
            nleft = self.minDepth(root.left)
            nright = self.minDepth(root.right)
            
            return min(nleft+1,nright+1)      