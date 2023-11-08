def miniMaxSum(arr):

    total = arr[0]
    lowest_value = arr[0]
    highest_value = arr[0]
    
    for i in arr[1:]:
        total += i
        
        if i < lowest_value:
            lowest_value = i
        if i > highest_value:
            highest_value = i
    
    max_sum = total - lowest_value
    min_sum = total - highest_value
    print (' '.join( [str(min_sum), str(max_sum)] ) )
    

def miniManSum2(arr):
    
    total = sum(arr)
    lowest_value = min(arr)
    highest_value = max(arr)
    
    max_sum = total - lowest_value
    min_sum = total - highest_value
    print (' '.join( [str(min_sum), str(max_sum)] ) )
