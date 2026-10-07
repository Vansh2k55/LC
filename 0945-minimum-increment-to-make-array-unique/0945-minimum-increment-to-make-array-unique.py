class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        112237
        nums.sort()
        ans=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc=nums[i-1]-nums[i]+1
                nums[i]+=inc
                ans+=inc
        return ans


        