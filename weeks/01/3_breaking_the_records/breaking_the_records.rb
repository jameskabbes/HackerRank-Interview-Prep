def breaking_records(scores)
    min_score = scores[0]
    max_score = scores[0]
    min_score_broken = 0
    max_score_broken = 0

    scores[1..-1].each do |score|
        # New max score
        if score > max_score
            max_score = score
            max_score_broken += 1
        end

        # New min score
        if score < min_score
            min_score = score
            min_score_broken += 1
        end
    end

    [max_score_broken, min_score_broken]
end