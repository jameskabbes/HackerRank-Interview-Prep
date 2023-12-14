# Lonely Integer

## Solutions

- [.js](lonely_integer.js)
- [.py](lonely_integer.py)
- [.rb](lonely_integer.rb)

## Explanation
In this example, we have an array of numbers. Each number in the array appears twice, except for one number, which only appears once. This example solves the problem utilizing the set data structure, although there are many other solutions. We define two sets, one set to track the first time we see a unique number, and the second set to capture the second (or third, or fourth) time we see that given number. Then, we simply return the only number which is found in the first set, but not the second set.

### Defining Sets
Define two sets: `appears_once` and `appears_twice`. 

* `appears_once`: will track all numbers that appear at least once in the array
* `appears_twice`: will track all numbers that appear at least twice in the array

**Note**: If we take the difference of `appears_once` and `appears_twice`, we will have a set of numbers which appear exactly one time (just what we are looking for!).

### Populating Sets
Next, loop through each item in the given array. If the item is not contained in the `appears_once` set, we add the number to the set. That means it is the first time we have seen the number.

If the item is already contained in the `appears_once` set, then this is not the first time we have seen that number. We will add this number to the `appears_twice` set instead. 

### Difference of Two Sets
Next, we get the difference of the two sets. As described above, `appears_once` - `appears_twice` gives us a set of numbers that occur exactly one time.

### Returning the Lonely Integer
Given the constraints of the prompt, this new `difference` set should only contain one number. Simply loop through the new set, and return the first number, the lonely integer.