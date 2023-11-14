function diagonalDifference(arr) {
    let primary_diagonal_sum = 0;
    let secondary_diagonal_sum = 0;
  
    for (let i = 0; i < arr.length; i++) {
      primary_diagonal_sum += arr[i][i];
      secondary_diagonal_sum += arr[i][arr.length - (i + 1)];
    }
  
    return Math.abs(primary_diagonal_sum - secondary_diagonal_sum);
  }
  