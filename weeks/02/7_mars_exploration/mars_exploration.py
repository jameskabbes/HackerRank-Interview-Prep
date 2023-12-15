def marsExploration(s):

    CORRECT_MESSAGE = 'SOS'
    changed_letters = 0

    for i in range(len(s)):
        if s[i] != CORRECT_MESSAGE[i % len(CORRECT_MESSAGE)]:
            changed_letters += 1

    return changed_letters
