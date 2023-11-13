function matchingStrings(strings, queries) {

    const stringCounts = {};

    for (let string of strings) {
        if (!stringCounts[string]) {
            stringCounts[string] = 1;
        } else {
            stringCounts[string]++;
        }
    }

    const queryCounts = [];

    for (let query of queries) {
        if (stringCounts[query]) {
            queryCounts.push(stringCounts[query]);
        } else {
            queryCounts.push(0);
        }
    }

    return queryCounts;


}