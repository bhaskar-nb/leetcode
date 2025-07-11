class Solution {
    public int climbStairs(int n) {
       int[]dp=new int[n+1];
        for(int i=0;i<=n;i++){
            dp[i]=-1;
        }
        return totalways(n,dp);
    }
    public static int totalways(int n,int dp[]){
        if(n==0||n==1){
            return 1;
        }
        if(dp[n]!=-1){
            return dp[n];
        }
        dp[n]=totalways(n-1,dp)+totalways(n-2,dp);
        return dp[n];
    }
}