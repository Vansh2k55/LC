class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        leftsum=0
        rightsum=0
        for i in range(len(nums)):
            leftsum+=nums[i]
            left[i]=leftsum
            
        for i in range(len(nums)-1,-1,-1):
            rightsum+=nums[i]
            right[i]=rightsum
        for i in range(len(left)):
            if left[i]==right[i]:
                return i
        return -1

        