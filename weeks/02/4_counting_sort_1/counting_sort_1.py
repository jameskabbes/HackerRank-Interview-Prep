def countingSort(arr):
    
    freq_array = [ 0 for i in range(100)]

    for integer in arr:
        freq_array[ integer ] += 1
        
    return freq_array
    
