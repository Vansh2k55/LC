class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd=float('inf')
        min_even=float('inf')
        for value in nums1:
            if value%2:
                min_odd=min(value,min_odd)
            else:
                min_even=min(value,min_even)
        if min_even>min_odd:
            return True
        if min_even==float('inf') or min_odd==float('inf'):
            return True
        else:
            return False