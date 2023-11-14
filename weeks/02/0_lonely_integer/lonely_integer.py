def lonelyinteger(a):

    appears_once = set()
    appears_twice = set()
    
    for item in a:
        if item not in appears_once:
            appears_once.add( item )
        else:
            appears_twice.add( item )
        
    for item in appears_once:
        if item not in appears_twice:
            return item