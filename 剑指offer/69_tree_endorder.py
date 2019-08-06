# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def endorder(self, root):
#         if root is None:
#             return ''
#         if root.lef:
#             self.midorder(root.left)
#         print (root.val)
#         if root.right:
#             self.midorder(root.right)

class Solution(object):
    def endorder(self, root):
        res = []
        if root:
            res += self.endorder(root.left)
            res.append(root.val)
            res += self.endorder(root.right)