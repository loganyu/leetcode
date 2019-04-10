class MaxHeap
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
    while (has_parent?(index) && parent(index) < @items[index])
      swap(get_parent_index(index), index)
      index = get_parent_index(index)
    end
  end

  def heapify_down
    index = 0
    while (has_left_child?(index))
      larger_child_index = get_left_child_index(index)
      if has_right_child?(index) && right_child(index) > left_child(index)
        larger_child_index = get_right_child_index(index)
      end

      if @items[index] > @items[larger_child_index]
        break
      else
        swap(index, larger_child_index)
      end
      index = larger_child_index
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