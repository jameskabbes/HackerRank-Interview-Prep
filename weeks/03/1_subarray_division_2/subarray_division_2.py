def birthday(s, d, m):

    solutions = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            solutions += 1
    return solutions
