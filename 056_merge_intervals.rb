# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    sol = []
    intervals.sort_by{|s,e| s}.each do |interval|
        if sol.empty? || sol[-1][1] < interval[0]
            sol << interval
        else
            if sol[-1][1] < interval[1]
                sol[-1][1] = interval[1]
            end
        end
    end
    
    sol
end
