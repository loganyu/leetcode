# @param {Integer} n
# @return {Boolean}
# O(log n)
def is_power_of_two(n)
    if n <= 0
        return false
    end
    while n % 2 == 0
        n /= 2
    end
    
    n == 1
end

# bitwise solution. O(1)
def is_power_of_two(n)
    if n <= 0
        return false;
    end
    
    return (n&(n-1)) == 0
end

# math derivation O(1)
def is_power_of_two(n)
    if n <= 0
        return false;
    end
    
    return 2**30 % n == 0
end

# bitcount O(1)
def is_power_of_two(n)
    return n > 0 && n.to_s(2).count("1") == 1
end