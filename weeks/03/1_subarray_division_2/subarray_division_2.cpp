int birthday(vector<int>& s, int d, int m) {
    int solutions = 0;
    for (size_t i = 0; i <= s.size() - m; ++i) {
        int sum = 0;
        for (size_t j = i; j < i + m; ++j) {
            sum += s[j];
        }
        if (sum == d) {
            solutions++;
        }
    }
    return solutions;
}
