/*
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
*/

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int sum = nums[0] + nums[1] + nums[nums.length - 1];
        int closestSum = sum;

        for(int i = 0; i < nums.length - 2; i++){
            if(i==0 || nums[i] != nums[i-1]){
                int left = i + 1, right = nums.length - 1;
                while(left < right){
                    sum = nums[left] + nums[right] + nums[i];
                    if (sum < target) {
                        while(left<right && nums[left] == nums[left+1]){
                            left++;
                        }
                        left++;
                    } else if(sum > target) {
                        while(left<right && nums[right] == nums[right-1]){
                            right--;
                        }
                        right--;
                    } else {
                        return sum;
                    }
                    if (Math.abs(target - sum) < Math.abs(target - closestSum)) {
                        closestSum = sum;
                    }
                }
            }

        }
        return closestSum;
    }
}

