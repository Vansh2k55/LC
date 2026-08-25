class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        t=k
        while t in nums:
            t=t+k
        return t
        