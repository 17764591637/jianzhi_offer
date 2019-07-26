'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return [] 
        res = []
        currentStack = [pRoot]
        while len(currentStack):
            list_node = []
            for t in currentStack:
                list_node.append(t.val)
            res.append(list_node)
            for i in range(len(currentStack)):
                node = currentStack.pop(0)
                if node.left:
                    currentStack.append(node.left)
                if node.right:
                    currentStack.append(node.right)

        return res


