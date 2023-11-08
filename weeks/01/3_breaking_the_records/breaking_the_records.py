def breakingRecords(scores):

    min_score = scores[0]
    max_score = scores[0]
    min_score_broken = 0
    max_score_broken = 0
    
    for score in scores[1:]:
        
        # new max score
        if score > max_score:
            max_score = score
            max_score_broken += 1
            
        # new min score
        if score < min_score:
            min_score = score
            min_score_broken += 1        

    return [ max_score_broken, min_score_broken ]
