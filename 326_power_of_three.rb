# @param {Integer} n
# @return {Boolean}
def is_power_of_three(n)
    # 3**19 is max int to power of 3
    return n > 0 && 3**19 % n == 0
end

# iterative
def is_power_of_three(n)
    if n > 1
        while n % 3 == 0
            n /= 3
        end
    end
    
    return n == 1
end

