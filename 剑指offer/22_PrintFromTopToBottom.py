'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return []
        currentStack = [root]#同一层的节点
        while len(currentStack):
            t = currentStack.pop(0)
            res.append(t.val)
            if t.left:
                currentStack.append(t.left)
            if t.right:
                currentStack.append(t.right)
        return res
