function breakingRecords(scores) {
    let minScore = scores[0];
    let maxScore = scores[0];
    let minScoreBroken = 0;
    let maxScoreBroken = 0;

    for (let i = 1; i < scores.length; i++) {
        let score = scores[i];

        // New max score
        if (score > maxScore) {
            maxScore = score;
            maxScoreBroken++;
        }

        // New min score
        if (score < minScore) {
            minScore = score;
            minScoreBroken++;
        }
    }

    return [maxScoreBroken, minScoreBroken];
}