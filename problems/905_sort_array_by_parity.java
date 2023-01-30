/*
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
*/

class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int i = 0;
        int j = nums.length - 1;
        while (i < j) {
            if (nums[i] % 2 == 1 && nums[j] % 2 == 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
            
            if (nums[i] % 2 == 0)
                i++;
            if (nums[j] % 2 == 1)
                j--;
        }
        
        return nums;
    }
}

