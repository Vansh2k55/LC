class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        if k==1:
            count=Counter(nums)
            ans=-1
            for i in range(len(nums)):
                if count[nums[i]]==1:
                    ans=max(ans,nums[i])
            return ans
        first=nums[0]
        last=nums[-1]
        first_valid=True
        last_valid=True
        for i in range(1,n):
            if nums[i]==first:
                first_valid=False
                break
        for i in range(n-2,-1,-1):
            if nums[i]==last:
                last_valid=False
                break
        if first_valid and last_valid:
            return max(first,last)
        elif first_valid:
            return first
        elif last_valid:
            return last
        else:
            return -1
        