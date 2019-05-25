=begin
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    map = {}
    nums.each do |num|
        map[num] ||= 0
        map[num] += 1
    end
    nums_by_freq = {}
    map.each do |num, freq|
        nums_by_freq[freq] ||= []
        nums_by_freq[freq] << num
    end
    
    min_heap = MinHeap.new
    
    map.values.each do |freq|
        min_heap.add(freq)
        if min_heap.size > k
            min_heap.poll
        end
    end
    
    k_most_frequent = []
    k.times do
        freq = min_heap.poll
        num = nums_by_freq[freq].pop
        k_most_frequent << num
    end
    
    k_most_frequent
end


class MinHeap
  def initialize(items = [])
    @items = []
    items.each do |item|
      self.add(item)
    end
  end

  def peek
    if @items.length == 0
      return raise "Heap Empty"
    end

    return @items[0]
  end

  def poll
    if @items.length == 0
      return raise "Heap Empty"
    end
    item = @items[0]
    @items[0] = @items[-1]
    @items.pop()
    heapify_down()

    return item
  end

  def add(item)
    @items.push(item)
    heapify_up()

    return true
  end

  def size
    return @items.count
  end

  private

  def heapify_up
    index = @items.length - 1
    while (has_parent?(index) && parent(index) > @items[index])
      swap(get_parent_index(index), index)
      index = get_parent_index(index)
    end
  end

  def heapify_down
    index = 0
    while (has_left_child?(index))
      smaller_child_index = get_left_child_index(index)
      if has_right_child?(index) && right_child(index) < left_child(index)
        smaller_child_index = get_right_child_index(index)
      end

      if @items[index] < @items[smaller_child_index]
        break
      else
        swap(index, smaller_child_index)
      end
      index = smaller_child_index
    end
  end

  def swap(i, j)
    @items[i], @items[j] = @items[j], @items[i]
  end

  def get_left_child_index(parent_index)
    return 2 * parent_index + 1
  end

  def get_right_child_index(parent_index)
    return 2 * parent_index + 2
  end

  def get_parent_index(child_index)
    return (child_index - 1) / 2
  end

  def has_left_child?(index)
    return get_left_child_index(index) < @items.length
  end

  def has_right_child?(index)
    return get_right_child_index(index) < @items.length
  end

  def has_parent?(index)
    return get_parent_index(index) >= 0
  end

  def left_child(index)
    return @items[get_left_child_index(index)]
  end

  def right_child(index)
    return @items[get_right_child_index(index)]
  end

  def parent(index)
    return @items[get_parent_index(index)]
  end
end

