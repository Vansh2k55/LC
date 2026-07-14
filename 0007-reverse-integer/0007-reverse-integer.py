class Solution(object):
    def reverse(self, x):
        if x < 0:
            ans = -int(str(-x)[::-1])
        elif x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = 0

        if -2**31 <= ans <= 2**31 - 1:
            return ans
        return 0