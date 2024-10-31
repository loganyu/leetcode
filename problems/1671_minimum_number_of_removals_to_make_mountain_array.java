/*
 * You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.



Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].


Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
*/

class Solution {
    private List<Integer> getLongestIncreasingSubsequenceLength(
        List<Integer> v
    ) {
        List<Integer> lisLen = new ArrayList<>(
            Collections.nCopies(v.size(), 1)
        );
        List<Integer> lis = new ArrayList<>();
        lis.add(v.get(0));

        for (int i = 1; i < v.size(); i++) {
            int index = lowerBound(lis, v.get(i));
            if (index == lis.size()) {
                lis.add(v.get(i));
            } else {
                lis.set(index, v.get(i));
            }
            lisLen.set(i, lis.size());
        }

        return lisLen;
    }

    private int lowerBound(List<Integer> lis, int target) {
        int left = 0, right = lis.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (lis.get(mid) >= target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public int minimumMountainRemovals(int[] nums) {
        int N = nums.length;
        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) numsList.add(num);
        List<Integer> lisLength = getLongestIncreasingSubsequenceLength(
            numsList
        );
        Collections.reverse(numsList);
        List<Integer> ldsLength = getLongestIncreasingSubsequenceLength(
            numsList
        );
        Collections.reverse(ldsLength);

        int minRemovals = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            if (lisLength.get(i) > 1 && ldsLength.get(i) > 1) {
                minRemovals = Math.min(
                    minRemovals,
                    N - lisLength.get(i) - ldsLength.get(i) + 1
                );
            }
        }

        return minRemovals;
    }
}

