def matchingStrings(strings, queries)
    string_counts = {}

    strings.each do |string|
        if string_counts[string]
            string_counts[string] += 1
        else
            string_counts[string] = 1
        end
    end

    query_counts = []

    queries.each do |query|
        if string_counts[query]
            query_counts << string_counts[query]
        else
            query_counts << 0
        end
    end

    query_counts
end