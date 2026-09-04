# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
       


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    def pushLeft(self, node):

        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()

        if node.right:
            self.pushLeft(node.right)

        return node.val

    def hasNext(self):
        return len(self.stack) > 0