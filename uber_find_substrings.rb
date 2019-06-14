=begin
Input: words = ["Apple", "Melon", "Orange", "Watermelon"], parts = ["a", "mel", "lon", "el", "An"]
Output: ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]
=end

def find_substrings(words, parts)
  parts = parts.sort_by{|w| -w.length}
  sol = []
  words.each do |word|
    word_found = false
    parts.each do |part|
      if word_found
        break
      end
      (0...word.length).each do |i|
        if i + part.length > word.length
          break
        end

        if word[i...i+part.length] == part
          word.insert(i+part.length,"]")
          word.insert(i, "[")
          sol << word
          word_found = true
          break
        end
      end
    end
    if !word_found
      sol << word
    end
  end
  return sol
end

words = ["Apple", "Melon", "Orange", "Watermelon"]
parts = ["a", "mel", "lon", "el", "An"]
puts find_substrings(words, parts).inspect