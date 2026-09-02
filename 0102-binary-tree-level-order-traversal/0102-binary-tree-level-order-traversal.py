# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        from collections import deque

        result = []

        if root is None:
            return result

        q = deque([root])

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level)

        return result

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        