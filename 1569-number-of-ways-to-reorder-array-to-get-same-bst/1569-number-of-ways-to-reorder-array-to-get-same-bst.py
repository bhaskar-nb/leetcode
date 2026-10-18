from typing import List
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) < 3:
                return 1

            root = arr[0]

            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left_ways = dfs(left)
            right_ways = dfs(right)

            ways_to_merge = comb(len(left) + len(right), len(left))

            return (ways_to_merge * left_ways * right_ways) % MOD

        return (dfs(nums) - 1) % MOD