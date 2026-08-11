class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        summ=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break
            summ+=nums[i]
        num=set(nums)
        for _ in range(100):
            if summ not in num:
                return summ
            else:
                summ+=1
        


        