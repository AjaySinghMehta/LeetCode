# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        dummy = TreeNode(0)
        current = root
        prev = dummy

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            prev.right = current
            current.left = None
            prev = current
            current = current.right

        return dummy.right