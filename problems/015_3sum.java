/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
*/

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> triplets = new HashSet<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++) {
            int l = i + 1;
            int r = nums.length - 1;
            if (nums[i] > 0)
                break;
            while (l < r) {
                int total = nums[i] + nums[l] + nums[r];
                if (total == 0) {
                    triplets.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                } else if (total > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        
        return new ArrayList<>(triplets);
    }
}

