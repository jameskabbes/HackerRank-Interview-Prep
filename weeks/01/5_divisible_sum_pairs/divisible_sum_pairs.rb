def divisibleSumPairs(n, k, ar)
    valid_pairs = 0
    (0...n-1).each do |i|
        (i+1...n).each do |j|
            # Is divisible
            if (ar[i] + ar[j]) % k == 0
                valid_pairs += 1
            end
        end
    end
    valid_pairs
end