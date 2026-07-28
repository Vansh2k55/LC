class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        left=sorted(s[:n//2])
        if n%2:
            middle=s[n//2]
        else:
            middle=""
        right=left[::-1]
        return "".join(left)+middle+"".join(right)