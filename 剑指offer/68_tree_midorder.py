# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def midorder(self, root):
#         if root is None:
#             return ''
#         if root.left:
#             self.midorder(root.left)
#         print(root.val)
#         if root.right:
#             self.midorder(root.right)

class Solution:
    def inorderTraversal(self, root):
        res = []
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        
        return res