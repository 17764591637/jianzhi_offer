'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#递归
# class Solution(object):
#     def isSymmetrical(self, pRoot):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if pRoot == None:
#             return True
        
#         return self.checkTwoTree(pRoot.left,pRoot.right)
    
#     def checkTwoTree(self, leftTree, rightTree):
#         if leftTree==None and rightTree==None:
#             return True
#         if leftTree!=None and rightTree==None:
#             return False
#         if leftTree==None and rightTree!=None:
#             return False
#         if leftTree.val != rightTree.val:
#             return False
#         left = self.checkTwoTree(leftTree.left,rightTree.right)
#         right = self.checkTwoTree(leftTree.right,rightTree.left)
        
#         return left and right
#迭代
class Solution(object):
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        node_list = [pRoot.left,pRoot.right]
        while node_list:
            symmetricLeft = node_list.pop(0)
            symmetricRight = node_list.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            node_list.append(symmetricLeft.left)
            node_list.append(symmetricRight.right)
            node_list.append(symmetricLeft.right)
            node_list.append(symmetricRight.left)
            
        return True




