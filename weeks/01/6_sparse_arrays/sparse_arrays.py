def matchingStrings(strings, queries):
    
    string_counts = {}
    for string in strings:
        if string not in string_counts:
            string_counts[ string ] = 1
        else:
            string_counts[ string ] += 1
    
    query_counts = []
    for query in queries:
        if query in string_counts:
            query_counts.append( string_counts[query] )    
        else:
            query_counts.append( 0 )

    return query_counts
    