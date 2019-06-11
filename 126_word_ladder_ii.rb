# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {String[][]}
def find_ladders(begin_word, end_word, word_list)
    if word_list.empty?
        return []
    end
    
    all_combo_dict = get_all_combo_dict(word_list)
    paths = []
    queue = [[begin_word]]
    visited = {}
    path_found = false
    while !queue.empty?
        new_visited = {}
        queue.count.times do
            path = queue.shift
            current_word = path[-1]
            neighbors = get_neighbors(current_word, all_combo_dict)
            neighbors.each do |word|
                if word == end_word
                    paths << path + [word]
                    path_found = true
                elsif !visited.include?(word)
                    new_visited[word] = true
                    queue.push(path + [word])
                end
            end
        end
        
        if path_found
            break
        end
        
        visited.merge!(new_visited)
    end
    
    paths
end

def get_all_combo_dict(word_list)
    l = word_list[0].length
    all_combo_dict = {}
    word_list.each do |word|
        (0...l).each do |i|
            generic_word = "#{word[0...i]}*#{word[i+1...l]}"
            all_combo_dict[generic_word] ||= []
            all_combo_dict[generic_word] << word
        end
    end
    
    return all_combo_dict
end

def get_neighbors(current_word, all_combo_dict)
    l = current_word.length
    neighbors = []
    (0...l).each do |i|
        intermediate_word = "#{current_word[0...i]}*#{current_word[i+1...l]}"
        if all_combo_dict[intermediate_word]
            neighbors.concat(all_combo_dict[intermediate_word])
        end
    end
    
    return neighbors
end