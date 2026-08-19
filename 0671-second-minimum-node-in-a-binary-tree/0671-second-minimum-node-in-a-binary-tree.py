# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans=float('inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            if node.val>root.val:
                ans=min(ans,node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if ans==float('inf'):
            return -1
        else:
            return ans
        