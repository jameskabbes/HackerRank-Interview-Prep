def plusMinus(arr)

    positive = 0
    negative = 0
    zero = 0

    arr.each do |item|
    if item > 0
        positive += 1
    elsif item < 0
        negative += 1
    else
        zero += 1
    end
    end

    puts (positive.to_f / arr.length).round(6)
    puts (negative.to_f / arr.length).round(6)
    puts (zero.to_f / arr.length).round(6)
    
    
end