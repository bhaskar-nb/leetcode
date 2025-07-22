class Solution
{
    public int findSum(int grid[][], int m, int n, int dp[][])
    {
        if(m == 0 && n == 0) return grid[0][0];
        if(m<0 || n<0) return Integer.MAX_VALUE;

        if(dp[m][n]!=-1) return dp[m][n];
        int top = findSum(grid,m-1,n,dp);
        int left = findSum(grid,m,n-1,dp);

        dp[m][n] = grid[m][n] + Math.min(top, left);
        return dp[m][n];
    }
    public int minPathSum(int[][] grid) 
    {
        int m = grid.length;
        int n = grid[0].length;
        int dp[][] = new int[m][n];

        for(int rows[]:dp)
        {
            Arrays.fill(rows, -1);
        }
        return findSum(grid, m-1, n-1, dp);
    }
}