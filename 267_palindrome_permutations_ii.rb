=begin
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
=end

# @param {String} s
# @return {String[]}
def generate_palindromes(s)
    @sol = Set.new
    freq = {}
    s.each_char do |char|
        freq[char] ||= 0
        freq[char] += 1
    end
    if freq.length == 1
        return [s]
    end
    even = []
    odd_char = nil
    freq.keys.each do |char|
        if freq[char] % 2 == 0
            even.concat([char]*(freq[char]/2))
        else
            # there only can be one odd char for permutations
            if !odd_char.nil?
                return []
            end
            if freq[char] > 1
                even.concat([char]*((freq[char]-1)/2))
            end
            odd_char = char
        end
    end
    permute(even, 0, odd_char)       
    
    return @sol.to_a
end

def permute(even, s, odd_char)
    if even.length == s
        @sol.add("#{even.join}#{odd_char}#{even.reverse.join}")
    else
        (s...even.length).each do |e|
            if even[s] != even[e] || s == e
                even[s], even[e] = even[e], even[s]
                permute(even, s + 1, odd_char)
                even[s], even[e] = even[e], even[s]
            end
        end
    end
end

# build path solution
# @param {String} s
# @return {String[]}
def generate_palindromes(s)
    freq = Hash.new(0)
    s.each_char {|char| freq[char] += 1}
    middle = freq.keys.select{|char| freq[char] % 2 == 1}
    if middle.length > 1
        return []
    end
    
    if middle.length == 1
        freq[middle[0]] -= 1
        total = s.length - 1
    else
        total = s.length
    end
    
    ans = []
    path = []
    
    permutate(total, middle, freq, path, ans)
    
    return ans
end

def permutate(total, middle, freq, path, ans)
    if total == 0
        ans << (path + middle + path.reverse).join
        return
    end
    freq.keys.each do |char|
        if freq[char] <= 0
            next
        end
        freq[char] -= 2
        path.push(char)
        permutate(total - 2, middle, freq, path, ans)
        freq[char] += 2
        path.pop()
    end
end
