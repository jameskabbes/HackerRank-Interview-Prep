def miniMaxSum(arr)
    total = arr[0]
    lowest_value = arr[0]
    highest_value = arr[0]
    
    arr[1..-1].each do |i|
        total += i
    
        lowest_value = i if i < lowest_value
        highest_value = i if i > highest_value
    end
    
    max_sum = total - lowest_value
    min_sum = total - highest_value
    puts "#{min_sum} #{max_sum}"
end