def lonelyinteger(a):

    appears_once = set()
    appears_twice = set()
    
    for item in a:
        if item not in appears_once:
            appears_once.add( item )
        else:
            appears_twice.add( item )
        
    difference = appears_once-appears_twice
    lonely = list(difference)[0]
    return lonely
