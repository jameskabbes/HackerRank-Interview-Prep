function divisibleSumPairs(n, k, ar) {
    let validPairs = 0;
    
    for (let i = 0; i < n-1; i++) {
        for (let j = i+1; j < n; j++) {
            // Is divisible
            if ((ar[i] + ar[j]) % k === 0) {
                validPairs++;
            }
        }
    }
    
    return validPairs;
}