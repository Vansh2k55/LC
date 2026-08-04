class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        x=min(nums)
        y=max(nums)
        ans=[]
        s=set(nums)
        for i in range(x+1,y):
            if i not in s:
                ans.append(i)
        return ans
        


            

