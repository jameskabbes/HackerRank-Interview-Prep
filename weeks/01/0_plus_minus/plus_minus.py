def plusMinus(arr):
    
    """given an array of numbers, print off the proportion of numbers that are 1. positive, 2. negative, and 3. zero"""
    
    positive = 0
    negative = 0
    zero = 0
    
    for item in arr:
        if item > 0:
            positive += 1
        elif item < 0:
            negative += 1
        else:
            zero += 1
        
    print ( round(positive/len(arr), 6) )
    print ( round(negative/len(arr), 6) )
    print ( round(zero/len(arr), 6) )
   
