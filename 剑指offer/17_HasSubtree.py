'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

判断是否为子树的步骤：
1、原二叉树走前序遍历，试图发现哪个节点的值和被判断子树的根节点相同；
如果一直到最后也没有找到那么肯定不是
2、如果找到了，就两个二叉树一起前序遍历，试图发现两个二叉树同时遍历完成，
且同样的左右子树遍历过程中的节点值均相同，同时遍历完成说明有相同的形状，
左右子树遍历过程中的节点值均相同说明两个二叉树不仅形状一样，值也是一样，则可以认为是子树。
'''

'''
树真的难啊 还没看懂 得找个人请教一下才行了
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#solution 1
# class Solution:
#     def HasSubtree(self, pRoot1, pRoot2):
#         # write code here
#         if not pRoot2 or not pRoot2:
#             return False
#         return self.is_subtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    
#     def is_subtree(self,A,B):
#         if not B:
#             return True
#         if not A or A.val != B.val:
#             return False
        
#         return self.is_subtree(A.left,B.left) and self.is_subtree(A.right,B.right)
#solution 2：

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        def convert(p):
            if p:
                return str(p.val) +  convert(p.left) + convert(p.right)
            else:
                return ""
        return convert(pRoot2) in convert(pRoot1) if pRoot2 else False