/*
 * Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
*/

class Solution {
    public String largestNumber(int[] nums) {
        String[] numStrings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numStrings[i] = Integer.toString(nums[i]);
        }

        Arrays.sort(numStrings, (a, b) -> (b + a).compareTo(a + b));

        if (numStrings[0].equals("0")) {
            return "0";
        }

        StringBuilder largestNum = new StringBuilder();
        for (String numStr : numStrings) {
            largestNum.append(numStr);
        }

        return largestNum.toString();
    }
}

