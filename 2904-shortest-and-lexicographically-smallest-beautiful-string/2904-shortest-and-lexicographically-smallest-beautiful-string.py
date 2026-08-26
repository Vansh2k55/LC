class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        one=0
        ans=""
        for right in range(len(s)):
            if s[right]=='1':
                one+=1
            
            while k==one:
                curr=s[left:right+1]
                if ans=="" or len(curr)<len(ans):
                    ans=curr
                if len(curr)==len(ans) and curr<ans:
                    ans=curr
                if s[left]=='1':
                    one-=1
                left+=1
        return ans
            


        