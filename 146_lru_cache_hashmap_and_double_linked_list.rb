=begin
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
=end

class Node
    attr_accessor :key, :value, :prev, :next
    
    def initialize(key = nil, value = nil)
        @key = key
        @value = value
        @prev = nil
        @next = nil
    end
end

class LRUCache
=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @capacity = capacity
        @cache = {}
        @head = Node.new
        @tail = Node.new
        @head.next = @tail
        @tail.prev = @head
    end
    
    def add_node(node)
        node.prev = @head
        node.next = @head.next
        
        @head.next.prev = node
        @head.next = node
    end
    
    def remove_node(node)
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    end
    
    def move_to_head(node)
        remove_node(node)
        add_node(node)
    end
    
    def pop_tail
        remove_node(@tail.prev)
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        node = @cache[key]
        if node.nil?
            return -1
        end
        move_to_head(node)
    
        node.value
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        if @cache[key]
            node = @cache[key]
            move_to_head(node)
            node.value = value
        else
            node = Node.new(key, value)
            @cache[key] = node
            add_node(node)
       
            if @cache.count > @capacity
                @cache.delete(@tail.prev.key)
                pop_tail()
            end
        end
    end
end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)