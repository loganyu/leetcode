# @param {Integer} n
# @return {String}
def count_and_say(n)
    counts = [[nil], [1]]
    1.upto(n) do |i|
        count = []
        n_cur = nil
        n_count = 0

        counts[i].each do |num|
            if n_cur.nil? || n_cur != num
                if !n_cur.nil?
                    count << n_count
                    count << n_cur
                end
                n_cur = num
                n_count = 1
            else
                n_count += 1
            end
        end
        count << n_count
        count << n_cur
        counts << count
    end
    
    counts[n].join
end

puts count_and_say(10).inspect