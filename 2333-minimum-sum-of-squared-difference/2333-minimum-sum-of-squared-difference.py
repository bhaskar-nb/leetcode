
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diffs)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce every difference to at most left.
        remaining = k - sum(max(0, d - left) for d in diffs)

        diffs = [min(d, left) for d in diffs]

        # Use any remaining operations to reduce positive differences.
        for i in range(len(diffs)):
            if remaining == 0:
                break
            if diffs[i] == left and left > 0:
                diffs[i] -= 1
                remaining -= 1

        return sum(d * d for d in diffs)
