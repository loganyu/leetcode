=begin
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
=end

# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    if s.empty? || t.empty?
        return ""
    end
    
    dict_t = {}
    t.each_char do |char|
        dict_t[char] ||= 0
        dict_t[char] += 1
    end
    required = dict_t.count
    l = 0
    r = 0
    formed = 0
    window_counts = {}
    # ans (window length, left, right)
    ans = [-1, 0, 0]
    while (r < s.length)
        char = s[r]
        window_counts[char] ||= 0
        window_counts[char] += 1
        
        if dict_t[char] && window_counts[char] == dict_t[char]
            formed += 1
        end
        
        while l <= r && formed == required
            char = s[l]
            if ans[0] == -1 || (r - l + 1) < ans[0]
                ans = [(r - l + 1), l, r]
            end
            window_counts[char] -= 1
            if dict_t[char] && window_counts[char] < dict_t[char]
                formed -= 1
            end
            l += 1
        end
        
        r += 1
    end
    
    if ans[0] == -1
        return ""
    end
    
    return s[ans[1]..ans[2]]
end