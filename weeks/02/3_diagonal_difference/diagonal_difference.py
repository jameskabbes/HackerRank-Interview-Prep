def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(len( arr )):
        primary_diagonal_sum += arr[ i ][ i ]
        secondary_diagonal_sum += arr[ i ][ len(arr)-(i+1) ]
    
    return abs( primary_diagonal_sum-secondary_diagonal_sum )       
