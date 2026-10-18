
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        ans = []

        for c in order:
            idx = ord(c) - ord('a')
            ans.append(c * count[idx])
            count[idx] = 0

        for i in range(26):
            if count[i] > 0:
                ans.append(chr(i + ord('a')) * count[i])

        return ''.join(ans)
