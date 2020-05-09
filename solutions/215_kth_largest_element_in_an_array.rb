=begin
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
=end

require './min_heap'

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}

# heap O(nlogk) time  and O(k) space
def find_kth_largest(nums, k)
    heap = MinHeap.new

    nums.each do |num|
        heap.add(num)
        if heap.size > k
            heap.poll()
        end
    end
    
    return heap.poll()
end

# quick select O(n^2) time and O(1) space
def find_kth_largest(nums, k)
    left = 0
    right = nums.length - 1
    k_smallest = nums.length - k
    loop do
        if left == right
            return nums[left]
        end
        pivot_index = left + rand(right - left)
        pivot_index = partition(nums, left, right, pivot_index)
        if k_smallest == pivot_index
            return nums[k_smallest]
        elsif k_smallest < pivot_index
            right = pivot_index - 1
        else
            left = pivot_index + 1
        end
    end
end

def partition(nums, left, right, pivot_index)
    pivot = nums[pivot_index]
    swap(nums, pivot_index, right)
    store_index = left
    (left).upto(right).each do |i|
        if nums[i] < pivot
            swap(nums, store_index, i)
            store_index += 1
        end
    end
    swap(nums, store_index, right)

    return store_index
end

def swap(nums, i, j)
    nums[i], nums[j] = nums[j], nums[i]
end
