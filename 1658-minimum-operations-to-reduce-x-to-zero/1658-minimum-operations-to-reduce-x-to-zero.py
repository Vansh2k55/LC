class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        s=sum(nums)
        longest=0
        summ=0
        target=s-x
        left=0
        if target<0:
            return -1
        if target==0:
            return n
        for right in range(len(nums)):
            summ+=nums[right]

            while summ>target:
                summ-=nums[left]
                left+=1
            if summ==target:
                longest=max(longest,(right-left+1))
        if longest==0:
            return -1
        return n-longest
            



        