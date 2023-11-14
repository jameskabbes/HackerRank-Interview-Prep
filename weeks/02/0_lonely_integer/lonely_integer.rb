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
  
    appears_once.each do |item|
      if !appears_twice.include?(item)
        return item
      end
    end
  end
  