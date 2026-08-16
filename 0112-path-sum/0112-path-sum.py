# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        TargetSum=targetSum
        def dfs(root,TargetSum):
            if root is None:
                return False
            TargetSum-=root.val
            if root.left is None and root.right is None:
                return TargetSum==0
            return dfs(root.left,TargetSum) or dfs(root.right,TargetSum)
        return dfs(root,TargetSum)
        