def divisibleSumPairs(n, k, ar):
    
    valid_pairs = 0
    for i in range( n-1 ):
        for j in range( i+1, n ):
            
            # is divisible
            if (ar[i]+ar[j]) % k == 0:
                valid_pairs += 1
    
    return valid_pairs