/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
*/

class Solution {
    public boolean search(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) return false;
        int end = n - 1;
        int start = 0;
        
        while (start <= end) {
            int mid = start + (end - start) / 2;
            
            if (nums[mid] == target) {
                return true;
            }
            
            if (!isBinarySearchHelpful(nums, start, nums[mid])) {
                start++;
                continue;
            }
            
            boolean pivotArray = existsInFirst(nums, start, nums[mid]);
            boolean targetArray = existsInFirst(nums, start, target);
            
            if (pivotArray ^ targetArray) {
                if (pivotArray) {
                    start = mid + 1;
                } else{
                    end = mid - 1;
                }
            } else {
                if (nums[mid] < target) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        
        return false;
    }
    
    private boolean isBinarySearchHelpful(int[] arr, int start, int element) {
        return arr[start] != element;
    }
    
    private boolean existsInFirst(int[] arr, int start, int element) {
        return arr[start] <= element;
    }
}

