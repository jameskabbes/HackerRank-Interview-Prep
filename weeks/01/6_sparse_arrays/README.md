# Sparse Arrays

## Solutions
* [.js](sparse_arrays.js)
* [.py](sparse_arrays.py)
* [.rb](sparse_arrays.rb)

## Explanation
In this problem, we need to be able to find how many times certain strings appear in an array. To do this, we will use a hash table / dictionary / map.

### string_counts
First, we define an empty hash called `string_counts`. In this hash, we will store strings as the key and the integer number of times they appear as values. `{ 'string': 3 }`

Looping through each string in `strings`, we keep track of the number of times we have seen each string. If the string is not found as a key in our hash (we have never seen this string before), then we add the string to our hash, with the key being the string, and the value being 1. 

If the string from the for loop is already a key in the `string_counts` map (we have seen it before), then we simply incremement its value by 1. If the value was 3 before, now it will be 4. This tracks how many times we have seen each unique string in the `strings` array.

### query_counts
Next, we are given an array of strings to "query", called `queries`. We will track the number of times each query appears in the `strings` array with a new array called `query_counts`. 

Looping through each `query` found in `queries`, we need to check how many times it appears in `strings`. We will do this using our already defined `string_counts` hash. 

If `query` **is not** a key in the `string_counts` hash, that means it was not present in the `strings` array, so its count would be 0. 0 is appended to the `query_counts` array.

If `query` **is** a key in the `string_counts` hash, then it appears 1 or more times in the `strings` array. We access the count by using the value of the `strings_count` hash at key of `query`. This value is appended to `query_counts`.

Finally, return the `query_counts` array.

