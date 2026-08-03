class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        z=0
        n=len(needle)
        while i<(len(haystack)):
            if j<len(haystack) and needle[z]==haystack[j]:
                if z==n-1:
                    return i
                j+=1

                z+=1
            else:
                i+=1
                j=i
                z=0
        return -1
