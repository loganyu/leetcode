/*
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
*/

class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length + 2;
        int[] new_nums = new int[n];
        
        for (int i = 0; i < nums.length; i++) {
            new_nums[i+1] = nums[i];
        }
        
        new_nums[0] = new_nums[n-1] = 1;
        
        int[][] memo = new int[n][n];
        
        return dp(memo, new_nums, 0, n-1);
    }
    
    public int dp(int[][] memo, int[] nums, int left, int right) {
        if (left + 1 == right) return 0;
        
        if (memo[left][right] > 0) return memo[left][right];
        
        int ans = 0;
        for (int i = left + 1; i < right; ++i) 
            ans = Math.max(ans, nums[left] * nums[i] * nums[right] + dp(memo, nums, left, i) + dp(memo, nums, i, right));
        memo[left][right] = ans;
       
        
        return ans;
    }
}

