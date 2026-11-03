class Solution:
    def minMoves(self, nums: List[int]) -> int:
        larg=max(nums)
        ans=0
        for i in range(len(nums)):
            ans+=larg-nums[i]
        return ans
        