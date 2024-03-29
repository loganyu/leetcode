=begin
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
=end

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    i = m + n - 1
    m -= 1
    n -= 1
    while(m >= 0 && n >= 0)
        if nums1[m] > nums2[n]
            nums1[i] = nums1[m]
            m -= 1
        else
            nums1[i] = nums2[n]
            n -= 1
        end
        i -= 1
    end
    if n >= 0
        nums1[0..i] = nums2[0..i]
    end
end
