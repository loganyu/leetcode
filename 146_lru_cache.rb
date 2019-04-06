=begin
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
=end

class LRUCache

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        @capacity = capacity
        @hash = {}
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        if @hash[key].nil?
            return -1
        end
        value = @hash.delete(key)
        @hash[key] = value
        
        return value
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        if @hash[key]
            @hash.delete(key)
        end
        @hash[key] = value
        if @hash.length > @capacity
            @hash.shift
        end
        
        return nil
    end


end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)