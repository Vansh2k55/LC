# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        path=[]
        def dfs(root,targetSum):
            if root is None:
                return 
            path.append(root.val)
            if root.left is None and root.right is None:
                if targetSum==root.val:
                    ans.append(path.copy())
            else:
                dfs(root.left,targetSum-root.val)
                dfs(root.right,targetSum-root.val)
            path.pop()
        dfs(root,targetSum)     
        return ans   