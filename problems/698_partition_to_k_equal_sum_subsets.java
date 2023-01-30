/*
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
*/

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        if (k > nums.length)
            return false;
        int sum = 0;
        for (int num : nums)
            sum += num;
        if (sum % k != 0)
            return false;
        boolean[] visited = new boolean[nums.length];
        Arrays.sort(nums);
        
        return dfs(nums, 0, nums.length - 1, visited, sum / k, k);
    }
    
    public boolean dfs(int[] nums, int sum, int st, boolean[] visited, int target, int round) {
        if (round == 0)
            return true;
        if (sum == target && dfs(nums, 0, nums.length - 1, visited, target, round - 1))
            return true;
        for (int i = st; i >= 0; i--) {
            if (!visited[i] && sum + nums[i] <= target) {
                visited[i] = true;
                if (dfs(nums, sum + nums[i], i - 1, visited, target, round))
                    return true;
                visited[i] = false;
            }
        }
        
        return false;
    }
}

