#include <iostream>
#include <string>
#include <unordered_set>

std::string pangrams(const std::string& s) {
    std::unordered_set<char> alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    std::unordered_set<char> string_set;

    for (char c : s) {
        string_set.insert(std::tolower(c));
    }

    for (char letter : alphabet) {
        if (string_set.find(letter) == string_set.end()) {
            return "not pangram";
        }
    }

    return "pangram";
}