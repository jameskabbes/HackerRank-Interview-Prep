# Subarray Division 2

## Solutions

- [.cpp](subarray_division_2.cpp)
- [.js](subarray_division_2.js)
- [.py](subarray_division_2.py)
- [.rb](subarray_division_2.rb)

## Explanation

One of the solutions to this problem is a follows.

Traversing through the array `s` in chunks of length `m`, check and see if the sum of the numbers contained in the chunk equals `d`.

First, we initialize a `solutions` counter, this will track the number of valid solutions that are present.

Keeping in mind the example given, follow along with the grid for the problem logic.

| s               | i   | i+m | s[ i:i+m ] | sum == d? |
| --------------- | --- | --- | ---------- | --------- |
| [**2,2**,1,3,2] | 0   | 2   | [2,2]      | yes       |
| [2,**2,1**,3,2] | 1   | 3   | [2,1]      | no        |
| [2,2,**1,3**,2] | 2   | 4   | [1,3]      | yes       |
| [2,2,1,**3,2**] | 3   | 5   | [3,2]      | no        |

After initializing the solutions, we call a for loop that returns the `i`'s that we need. From the example above, that gives us `[0,1,2,3]`.

Thinking at a high level, the pattern of which indices `i` to check starts with the length of `s` and subtracts the length of the chunk `m`, adding back 1 as a correction.

The for loop should loop through numbers `0, 1, 2 ... length(s) - m + 1`.

Now, inside the loop, find the sum of all numbers of
