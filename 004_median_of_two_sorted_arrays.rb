=begin
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
=end

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    a, b = [nums1, nums2].sort_by(&:size)
    m, n = a.size, b.size
    imin = 0
    imax = m
    half_len = (m + n + 1) / 2
    while imin <= imax
        i = (imin + imax) / 2
        j = half_len - i
        if i < m && b[j-1] > a[i]
            imin = i + 1
        elsif i > 0 && a[i-1] > b[j]
            imax = i - 1
        else
            if i == 0
                max_of_left = b[j-1]
            elsif j == 0
                max_of_left = a[i-1]
            else
                max_of_left = [a[i-1], b[j-1]].max
            end
            
            if (m + n) % 2 == 1
                return max_of_left
            end
            
            if i == m
                min_of_right = b[j]
            elsif j == n
                min_of_right = a[i]
            else
                min_of_right = [a[i], b[j]].min
            end
            
            return (max_of_left + min_of_right) / 2.0
        end
    end
end
