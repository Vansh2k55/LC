class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum=0
        low=nums[0]
        for i in range(len(nums)):
            presum+=nums[i]
            low=min(low,presum)
        if low>0:
            return 1
        else:
            return -(low-1)

        