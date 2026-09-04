class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            ans.append(pre)
        return ans