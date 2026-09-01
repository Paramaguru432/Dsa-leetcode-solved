# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):

        result = []

        def preorder(node):
            if node is None:
                return

            # Visit Root
            result.append(node.val)

            # Visit Left
            preorder(node.left)

            # Visit Right
            preorder(node.right)

        preorder(root)

        return result
