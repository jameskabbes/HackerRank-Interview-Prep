# Counting Sort 1

## Solutions

- [.js](counting_sort_1.js)
- [.py](counting_sort_1.py)
- [.rb](counting_sort_1.rb)

## Explanation

In this problem, we are asked to come up with a different way (a faster way) to sort an array.

As stated, comparision sorting requires checking if `array[0] < array[1]` and usually has a runtime of _n x log(n)_. However, in this instance, we are sorting a special kind of array. Specifically, each item in the array is an integer between 0-99. This special array allows us to sort things in a faster runtime.

The challenge asks us to turn this

`[1 2 2 3 4 3 0 1 2 0 1 1 ]`

into this

`[2 4 3 2 1 ]`

because in the list there are

- 2 zeros [0th index]
- 4 ones [1st index]
- 3 twos [2nd index]
- 2 threes [3rd index]
- 1 four [4th index]

Then, we can take this frequency array and return a sorted array like:

`[0,0,1,1,1,1,2,2,2,3,3,4]` using
`[ 0*2, 1*4, 2*3, 3*2, 4*1 ]`

### Solution

To make our frequency array, first **initialize an array of length 100 with values of 0**. We choose 100 because the array will contain integers that range from 0-99, or 100 different possibilies.

In our frequeny array, `freq_array`, the index of the array will correspond with the integer that was found in the original array. For example:

- `freq_array[3]` will contain the number of times the integer `3` appears
- `freq_array[0]` will contain the number of times the integer `0` appears
- `freq_array[99]` will contain the number of times the integer `99` appears
- etc.

Next, **loop through each integer given to us in the original array, keeping track of the number of occurrences**. At each number, increment the occurence count `freq_array[ integer ]` by 1.

At the end, the `freq_array` will contain the number of times each integer represented by the given index appears in the original array.
