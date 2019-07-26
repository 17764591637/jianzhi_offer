# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def graorder(self, root):
        if root is None:
            return ''
        queue = [root]
        while queue:
            res = []
            for item in queue:
                print(root.val)
                if item.left:
                    res.append(item.left)
                if item.right:
                    res.append(item.right)
            queue = res