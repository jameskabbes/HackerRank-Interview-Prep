def lonelyinteger(a)
    appears_once = Set.new
    appears_twice = Set.new
  
    a.each do |item|
      if !appears_once.include?(item)
        appears_once.add(item)
      else
        appears_twice.add(item)
      end
    end
  
    difference = appears_once - appears_twice
  
    lonely = difference.to_a[0]
    return lonely
  end
  
