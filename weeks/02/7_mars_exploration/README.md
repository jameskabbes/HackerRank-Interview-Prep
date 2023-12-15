# Mars Exploration

## Solutions

- [.cpp](mars_exploration.cpp)
- [.js](mars_exploration.js)
- [.py](mars_exploration.py)
- [.rb](mars_exploration.rb)

## Explanation

In this problem, we are tasked with finding how many characters in a given transmission differ from an expected transmission. The message is supposed to say `SOS` over and over, but some of the letters are jumbled.

Begin by defining `CORRECT_MESSAGE = 'SOS'` and a counter `changed_letters = 0`.

Next, loop through each index, `i`, of the transmitted message. While looping through each index, we check if the character of the transmitted string at the given index does not matches what `CORRECT_MESSAGE` expects it to be. If they do not match, increment `changed_letters` by 1.

Use the modulo operator to compare the transmitted string with the expected string. Check out the table below for an example.

- Transmitted String: `SOSTOTSOD`
- Repeating `CORRECT_MESSAGE`: `SOS`

| index | Transmitted String`[index]` | index modulo 3 | Repeating Message`[index modulu 3]` | Match? | changed_letters |
| ----- | --------------------------- | -------------- | ----------------------------------- | ------ | --------------- |
| 0     | S                           | 0              | S                                   | True   | 0               |
| 1     | 0                           | 1              | 0                                   | True   | 0               |
| 2     | S                           | 2              | S                                   | True   | 0               |
| 3     | T                           | 0              | S                                   | False  | 1               |
| 4     | 0                           | 1              | 0                                   | True   | 1               |
| 5     | T                           | 2              | S                                   | False  | 2               |
| 6     | S                           | 0              | S                                   | True   | 2               |
| 7     | 0                           | 1              | 0                                   | True   | 2               |
| 8     | D                           | 2              | S                                   | False  | 3               |
