/*
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
*/

class Solution {
    private void backtrack(int[] nums, int index, List<Integer> sequence,
            Set<List<Integer>> result) {
        if (index == nums.length) {
            if (sequence.size() >= 2) {
                result.add(new ArrayList<>(sequence));
            }
            return;
        }
        if (sequence.isEmpty() ||
                sequence.get(sequence.size() - 1) <= nums[index]) {
            sequence.add(nums[index]);
            backtrack(nums, index + 1, sequence, result);
            sequence.remove(sequence.size() - 1);
        }
        backtrack(nums, index + 1, sequence, result);
    }

    public List<List<Integer>> findSubsequences(int[] nums) {
        Set<List<Integer>> result = new HashSet<List<Integer>>();
        List<Integer> sequence = new ArrayList<Integer>();
        backtrack(nums, 0, sequence, result);
        return new ArrayList(result);
    }
}

