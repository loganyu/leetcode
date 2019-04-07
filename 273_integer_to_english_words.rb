=begin
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
=end

# @param {Integer} num
# @return {String}
def number_to_words(num)
    if num == 0
        return "Zero"
    end
    
    billion = num / 1_000_000_000
    million = (num % 1_000_000_000) / 1_000_000
    thousand = (num % 1_000_000) / 1_000
    rest = (num % 1_000)
    
    result = ""
    if billion > 0
        result += "#{three(billion)} Billion "
    end
    if million > 0
        result += "#{three(million)} Million "
    end
    if thousand > 0
        result  += "#{three(thousand)} Thousand "
    end
    if rest > 0
        result += "#{three(rest)} "
    end
    
    return result[0..-2]
end

def three(num)
    hundred = num / 100
    rest = num % 100
    if hundred > 0 and rest > 0
        return "#{one(hundred)} Hundred #{two(rest)}"
    elsif hundred > 0
        return "#{one(hundred)} Hundred"
    elsif rest > 0
        return "#{two(rest)}"
    end
end

def two(num)
    if num == 0
        return ''
    elsif num < 10
        return one(num)
    elsif num < 20
        return two_less_20(num)
    else
        tenner = num / 10
        rest = num % 10
        if rest > 0
            return "#{ten(tenner)} #{one(rest)}"
        else
            return ten(tenner)
        end
    end
end

def ten(num)
    switcher = {
        2 => "Twenty",
        3 => "Thirty",
        4 => "Forty",
        5 => "Fifty", 
        6 => "Sixty", 
        7 => "Seventy", 
        8 => "Eighty", 
        9 => "Ninety", 
    }

    return switcher[num]
end

def two_less_20(num)
    switcher = {
        10 => "Ten",
        11 => "Eleven",
        12 => "Twelve",
        13 => "Thirteen",
        14 => "Fourteen",
        15 => "Fifteen",
        16 => "Sixteen",
        17 => "Seventeen",
        18 => "Eighteen",
        19 => "Nineteen",
    }
    
    return switcher[num]
end

def one(num)
    switcher = {
        1 => "One",
        2 => "Two",
        3 => "Three",
        4 => "Four",
        5 => "Five", 
        6 => "Six", 
        7 => "Seven", 
        8 => "Eight", 
        9 => "Nine", 
    }
    
    return switcher[num]
end

