class Solution(object):
    def climbStairs(self, n):
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]
