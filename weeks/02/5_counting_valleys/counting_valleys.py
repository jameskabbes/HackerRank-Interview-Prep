def countingValleys(steps, path):

    inMountain = False
    inValley = False

    mountains = 0
    valleys = 0
    elevation = 0

    for p in path:

        if p == 'D':
            if elevation == 0:
                inValley = True
            elevation -= 1

        if p == 'U':
            if elevation == 0:
                inMountain = True
            elevation += 1

        if elevation == 0:
            if inMountain:
                mountains += 1
            if inValley:
                valleys += 1
            inMountain = False
            inValley = False

    return valleys


print(countingValleys(12, list('DDUUDDUDUUUD')))
