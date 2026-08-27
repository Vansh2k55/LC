# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque([root])
        ans=[]
        level=0
        while q:
            levelnodes=[]
            for _ in range(len(q)):
                node=q.popleft()
                levelnodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level%2!=0:
                values=[node.val for node in levelnodes][::-1]
                for i in range(len(levelnodes)):
                    levelnodes[i].val=values[i]
            level+=1
        return root


        