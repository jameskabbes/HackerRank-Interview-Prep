def countingSort(arr)
    
    freq_array = Array.new(100, 0)

    arr.each do |integer|
        freq_array[ integer ] += 1
    end

    return freq_array
end    
