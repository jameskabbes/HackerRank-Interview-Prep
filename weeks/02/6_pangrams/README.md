# Pangrams

## Solutions

- [.py](pangrams.py)

## Explanation

In this problem, we need to check if a sentence `s` uses every letter in the alphabet. There are several ways to solve this, but this solution uses sets.

- Define a set called `alphabet`. Make its contents all 26 lowercase letters.
- Make each character in `s` lowercase. Cast the each character in the string into a set. Call it `string_set`.
- Loop through each `letter` in `alphabet`. Check if given `letter` is found in `string_set`.
  - If `letter` from alphabet is not found in `string_set`, immediately `return 'not pangram'`
  - If we make it through the entire alphabet and each `letter` is contained in `string_set`, `return 'pangram'`
