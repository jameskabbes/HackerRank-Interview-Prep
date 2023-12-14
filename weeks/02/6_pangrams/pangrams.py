def pangrams(s):

    alphabet = set(list('abcdefghijklmnopqrstuvwxyz'))
    string_set = set(list(s.lower()))

    for letter in alphabet:
        if letter not in string_set:
            return 'not pangram'

    return 'pangram'
