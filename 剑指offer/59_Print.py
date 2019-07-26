'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return [] 
        res = []
        currentStack = [pRoot]
        count = 1
        while len(currentStack):
            list_node = []
            for t in currentStack:
                list_node.append(t.val)
            if count % 2 == 0:
                list_node.reverse()

            res.append(list_node)
            count += 1
            
            for i in range(len(currentStack)):
                node = currentStack.pop(0)
                if node.left:
                    currentStack.append(node.left)
                if node.right:
                    currentStack.append(node.right)
               
        return res 
                
