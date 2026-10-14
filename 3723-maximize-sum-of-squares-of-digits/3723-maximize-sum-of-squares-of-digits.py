
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        nines, remainder = divmod(sum, 9)

        result = "9" * nines

        if remainder:
            result += str(remainder)

        result += "0" * (num - len(result))

        return result
