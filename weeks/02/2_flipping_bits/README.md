# Flipping Bits

## Solutions
* [.js](flipping_bits.js)
* [.py](flipping_bits.py)
* [.rb](flipping_bits.rb)

## Explanation
To solve this problem, we need to have a basic understanding of Base-10 versus Base-2 (binary) numbers. Read more about a binary number [here](https://en.wikipedia.org/wiki/Binary_number). To solve, we convert a Base-10 number into binary, switch each of the bits (1 -> 0, 0 -> 1) in the 32-bit number, and then convert back to Base-10. 

### Converting to Binary
Depending on the programming language used, there are different ways to convert an integer into a binary representation. The number 9 in Base-10 is written as `1001` in binary. That is the first step. Use a builtin conversion like `bin()` in Python or `toString()` in JavaScript.

| Base-10 | Base-2 (Binary) |
|---------|-----------------|
|0|0|
|1|1|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|
|7|111|
|8|1000|
|9|1001|

### Prep for 32 bits
The problem specifies that we are to use 32-bit unsigned integers. 

* Our starter 32-bit integer `bits`: `00000000000000000000000000000000`

To represent our example of 9, or `1001` as a 32-bit integer, we need to overwrite the last four bits of our empty integer with `1001`

* After inserting `1001` at the end, we have: `00000000000000000000000000001001`

In the code, this is done with a for loop. By looping over the digits in `1001`, we replace 

### Flip all bits
Now that our number represented as a 32-bit integer, we are asked to flip each bit. By using a for loop, flip the value of the bit found at each index.

* `1` -> `0`
* `0` -> `1`

### Convert to Base-10
After flipping the bits, convert this binary string into a Base-10 integer. To do this use something like `int()` in Python or `parseInt()` in JavaScript. Be sure to specifiy that this number is Base-2.

Return the newly converted Base-10 integer.