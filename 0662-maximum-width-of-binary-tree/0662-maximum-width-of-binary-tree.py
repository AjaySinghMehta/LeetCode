# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
          
        q.append([root,0])
        ans = 0
        while(q):
            n = len(q)
            ans = max(q[-1][1]-q[0][1]+1, ans)
            for i in range(n):
                front = q.popleft()
                if(front[0].left):
                    q.append([front[0].left,front[1]*2+1])
                if(front[0].right):
                    q.append([front[0].right, front[1]*2+2])
        return ans