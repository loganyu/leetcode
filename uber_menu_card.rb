def combos(menu, amount)
  menu = menu.sort_by{|item,price| -price}
  combos = []
  backtrack(menu, combos, amount, [], 0)

  return combos
end

def backtrack(menu, combos, amount, curr, m_start_idx)
  if amount - curr.sum{|item,price| price} < menu[-1][1]
    combos << curr.map{|item, price| item}
    return
  end

  (m_start_idx...menu.length).each do |i|
    if amount - curr.sum{|item,price| price} >= menu[i][1]
      curr.push(menu[i])
      backtrack(menu, combos, amount, curr, i)
      curr.pop()
    end
  end
end

menu = {
  "Noodle" => 12.87,
  "Rice" => 8.23,
  "Soup" => 5.76,
  "Coke" => 3.12,
  "Pepsi" => 3.12,
  "Pizza" => 10.89,
}

puts combos(menu, 30).inspect