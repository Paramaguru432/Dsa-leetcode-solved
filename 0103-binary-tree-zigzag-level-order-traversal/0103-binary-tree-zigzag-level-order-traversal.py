# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        from collections import deque
        result = []

        if root is None:
            return result

        queue = deque([root])
        left_to_right = True

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()

            result.append(level)

            left_to_right = not left_to_right

        return result
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        