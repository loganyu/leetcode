def choose_driver(drivers, n)
  driver = drivers[0]
  (1...n).each do |i|
    j = rand(i)
    if j == 0
      driver = drivers[j]
    end
  end
end

def choose_drivers(drivers, k, n)
  selected = []
  selected[0...k] = drivers[0...k]
  i = k
  while i < n
    j = rand(i+1)
    if j < k
      selected[j] = drivers[i]
    end
  end

  return selected
end

