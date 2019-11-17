=begin
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
=end

# Trie solution is TLE when run
class AutocompleteSystem

=begin
    :type sentences: String[]
    :type times: Integer[]
=end
    def initialize(sentences, times)
        @root = Trie.new
        @cur_sent = ""
        sentences.length.times.each do |i|
            insert(sentences[i], times[i])
        end
    end


=begin
    :type c: Character
    :rtype: String[]
=end
    def input(c)
        if c == '#'
            insert(@cur_sent, 1)
            @cur_sent = ""
            return []
        else
            @cur_sent += c
            list = lookup()
            return list.
                sort_by{|n| [-n.times, n.sentence]}.
                take(3).
                map(&:sentence)
        end
    end
    
    private

    def insert(sentence, times)
        trie = @root
        sentence.each_char do |char|
            i = get_i(char)
            trie.branches[i] ||= Trie.new
            trie = trie.branches[i]
        end
        
        trie.times += times
    end
    
    def get_i(char)
       if char == " "
           return 26
       else
           return char.ord - 'a'.ord
       end
    end
    
    def lookup
        trie = @root
        list = []
        @cur_sent.each_char do |char|
            i = get_i(char)
            if trie.branches[i].nil?
                return list
            end
            trie = trie.branches[i]
        end
        traverse(@cur_sent, trie, list)
        
        return list
    end
    
    def traverse(s, trie, list)
        if trie.times > 0
            list << Node.new(s, trie.times)
        end
        ('a'..'z').each do |char|
            i = get_i(char)
            if !trie.branches[i].nil?
                traverse(s+char, trie.branches[i], list)
            end
        end
        if !trie.branches[26].nil?
            traverse(s+' ', trie.branches[26], list)
        end
    end
end

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem.new(sentences, times)
# param_1 = obj.input(c)

class Node
    attr_accessor :sentence, :times
    def initialize(sentence, times)
        @sentence = sentence
        @times = times
    end
end

class Trie
    attr_accessor :branches, :times
    def initialize
        @branches = Array.new(27)
        @times = 0
    end
end


# One level indexing solution
class AutocompleteSystem

=begin
    :type sentences: String[]
    :type times: Integer[]
=end
    def initialize(sentences, times)
        @arr = Array.new(26){{}}
        @cur_sent = ""
        sentences.length.times.each do |i|
            idx = get_i(sentences[i][0])
            @arr[idx][sentences[i]] = times[i]
        end
    end


=begin
    :type c: Character
    :rtype: String[]
=end
    def input(c)
        if c == '#'
            i = get_i(@cur_sent[0])
            @arr[i][@cur_sent] ||= 0
            @arr[i][@cur_sent] += 1
            @cur_sent = ""
            return []
        else
            list = []
            @cur_sent += c
            i = get_i(@cur_sent[0])
            @arr[i].each do |sentence, times|
                if sentence.index(@cur_sent) == 0
                    list << Node.new(sentence, times)
                end
            end
            
            return list.
                sort_by{|n| [-n.times, n.sentence]}.
                take(3).
                map(&:sentence)
        end
    end
    
    private

    def get_i(char)
       if char == " "
           return 26
       else
           return char.ord - 'a'.ord
       end
    end
end

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem.new(sentences, times)
# param_1 = obj.input(c)

class Node
    attr_accessor :sentence, :times
    def initialize(sentence, times)
        @sentence = sentence
        @times = times
    end
end

class Trie
    attr_accessor :branches, :times
    def initialize
        @branches = Array.new(27)
        @times = 0
    end
end
