int marsExploration(string s) {
    const std::string CORRECT_MESSAGE = "SOS";
    int changedLetters = 0;

    for (size_t i = 0; i < s.length(); i++) {
        if (s[i] != CORRECT_MESSAGE[i % CORRECT_MESSAGE.length()]) {
            changedLetters++;
        }
    }

    return changedLetters;

}
