# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def preorder(self, root):
#         if root is None:
#             return ''
#         print(root.val)
#         if root.left:
#             self.preorder(root.left)
#         if root.right:
#             self.preorder(root.right)

class Solution(object):
    def preorder(self, root):
        res = []   
        if root:
            res.append(root.val)
            res += self.preorder(root.left)
            res += self.preorder(root.right)