class Solution(object):
    def diagonalSort(self, mat):
        from collections import defaultdict
        
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        for key in diagonals:
            diagonals[key].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()
        
        return mat
