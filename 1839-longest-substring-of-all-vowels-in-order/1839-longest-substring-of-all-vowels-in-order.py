class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word)==1:
            return 0
        count=defaultdict(int)
        left=0
        ans=0
        for right in range(len(word)):
            if right>0 and word[right]<word[right-1]:
                left=right
                count=defaultdict(int)
            count[word[right]]+=1
            if count['a']>0 and count['e']>0 and count['i']>0 and count['o']>0 and count['u']>0:
                ans=max(ans,right-left+1)
        return ans

        