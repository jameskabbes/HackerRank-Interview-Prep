def gradingStudents(grades):
    
    for i in range(len(grades)):
        grades[i] = grade( grades[i] )
    
    return grades

def grade( score ):

    if score < 38:
        return score
    
    mod = score % 5
    if mod == 3 or mod == 4:
        return score + (5-mod)
    
    return score
    
