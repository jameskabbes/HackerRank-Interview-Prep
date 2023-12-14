# Divisible Sum Pairs

## Solutions

- [.js](divisible_sum_pairs.js)
- [.py](divisible_sum_pairs.py)
- [.rb](divisible_sum_pairs.rb)

## Explanation

To start, we define a variable called `valid_pairs`. This will be used to keep track of the number of valid pairs of integers we encounter.

### i < j
One of the stipulations set aside for a valid pair of integers is that the index `i` of the first integer must be lower than the index of the second integer `j`. Next, you must find all pairs of integers in the array where `i < j`.

An easy way to do to this is with two for loops. The first for loop, with variable `i`, will loop through the first item, all the way to the second to last item. Within the first for loop, we start an additional for loop, with variable `j`. To ensure `i < j`, start `j` at the value of `i+1`. This loop will proceed all the way to the last item. 

This ensures that all pairs of integers where `i < j` are generated.

### checking divisible by k
To check if a number `x` is divisble by another number `y`, we use the modulo operator to check the remainder of the division of the two numbers. When `x mod y == 0`, this means `x` is divisble by `y`. The modulu operator differs per language.

### putting it all together
At each `i` | `j` pair, we calculate the sum of `array[i]` and `array[j]` and check if that sum is divisble by the given variable `k`. If so, we increment the `valid_pairs` counter by 1. Return the `valid_pairs` counter at the end of the function.