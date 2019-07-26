'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    
中，按结点数值大小顺序第三小结点的值为4。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 方法一：
# class Solution:
#     # 返回对应节点TreeNode
#     def KthNode(self, pRoot, k):
#         # write code here
#         list_node = []
#         if pRoot == None or k <= 0:
#             return None 
#         currentStack = [pRoot]
#         while len(currentStack):
#             t = currentStack.pop(0)
#             list_node.append(t)
#             if t.left:
#                 currentStack.append(t.left)
#             if t.right:
#                 currentStack.append(t.right)
#         list_node = sorted(list_node,key = lambda x:x.val)
#         if k>len(list_node):
#             return None
            
#         return list_node[k-1]

#方法二：
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #第三个节点是4
        #前序遍历5324768
        #中序遍历2345678
        #后序遍历2436875
        #所以是中序遍历，左->根->右
        global result
        result=[]
        self.midnode(pRoot)
        if  k<=0 or len(result)<k:
            return None
        else:
            return result[k-1]
              
    def midnode(self,root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)