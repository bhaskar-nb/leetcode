class Solution 
{
    public int totalWays(int m,int n,int dp[][])
    {
        if(m==0 || n==0)
        {
            return 1;
        }
        if(dp[m][n]!=-1)
        {
            return dp[m][n];
        }
        dp[m][n] = totalWays(m-1,n,dp)+totalWays(m,n-1,dp);
        return dp[m][n];
    }
    public int uniquePaths(int m, int n) 
    {
        int dp[][] = new int[m][n];
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i][j] = -1;
            }
        }
        return totalWays(m-1,n-1,dp);
    }
}