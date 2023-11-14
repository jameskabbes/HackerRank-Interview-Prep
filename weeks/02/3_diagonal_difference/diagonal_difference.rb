def diagonalDifference(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
  
    (0...arr.length).each do |i|
      primary_diagonal_sum += arr[i][i]
      secondary_diagonal_sum += arr[i][arr.length - (i + 1)]
    end
  
    return (primary_diagonal_sum - secondary_diagonal_sum).abs
  end
  