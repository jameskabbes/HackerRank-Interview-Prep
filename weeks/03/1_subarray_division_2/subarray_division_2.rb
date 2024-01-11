def birthday(s, d, m)
    solutions = 0
    (0..s.length - m).each do |i|
        sum = s[i, m].sum
        if sum == d
            solutions += 1
        end
    end
    solutions
end