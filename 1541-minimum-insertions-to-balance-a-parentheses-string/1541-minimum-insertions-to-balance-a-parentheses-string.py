
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # Check whether the next character is also ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert the missing closing parenthesis
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert an opening parenthesis
                    insertions += 1

            i += 1

        # Each remaining '(' needs two closing parentheses
        return insertions + 2 * open_count
