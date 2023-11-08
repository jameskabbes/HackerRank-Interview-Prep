# Mini-Max Sum

## Solutions
* [.js](mini_max_sum.js)
* [.py](mini_max_sum.py)
* [.rb](mini_max_sum.rb)

## Explanation
In this problem, we are given an array and we need to know three things about it:

* `total`: the sum of all numbers in the array
* `lowest_value`: the lowest value in the array
* `highest_value`: the highest value in the array

There are many ways to find these three values. You can use builtin functions like `sum()`, `min()`, `max()`. You can also loop through the array and keep track of each value as you go.

In many examples given, the values `total`, `lowest_value`, and `highest_value` are initialized as the first item in the array. We can safely do this since the constraints of the prompt say that the array will contain at least one item. Next, loop through the rest of the array (ignoring the first item). Add each item to cumulative total variable, and check if each item overtakes the current `lowest_value` or `highest_value`.

Once you have found the three values, you can calculate:
* `max_sum`: by taking `total`, the sum of entire array and subtracting the `lowest_value`
* `min_sum`: by taking `total`, the sum of entire array and subtracting the `highest_value`

Then, print off `min_sum` and `max_sum`, separated by a space.