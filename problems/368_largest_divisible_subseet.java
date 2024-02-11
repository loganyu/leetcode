/*
 * Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
*/

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length;
        if (n == 0) return new ArrayList();
        List<ArrayList> EDS = new ArrayList();
        for (int num : nums) EDS.add(new ArrayList());
        Arrays.sort(nums);
        for (int i = 0; i < n; ++i) {
        List<Integer> maxSubset = new ArrayList();
        for (int k = 0; k < i; ++k)
            if (nums[i] % nums[k] == 0 && maxSubset.size() < EDS.get(k).size())
            maxSubset = EDS.get(k);
        EDS.get(i).addAll(maxSubset);
        EDS.get(i).add(nums[i]);
        }
        List<Integer> ret = new ArrayList();
        for (int i = 0; i < n; ++i)
        if (ret.size() < EDS.get(i).size()) ret = EDS.get(i);
        return ret;
    }
}
