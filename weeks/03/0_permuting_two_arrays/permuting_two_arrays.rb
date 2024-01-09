def twoArrays(k, a, b)
    a.sort!
    b.sort!.reverse!
  
    a.each_with_index do |_, i|
      if a[i] + b[i] < k
        return 'NO'
      end
    end
  
    return 'YES'
  end
  