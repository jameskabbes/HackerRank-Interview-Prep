# Permuting Two Arrays

## Solutions

- [.cpp](permuting_two_arrays.cpp)
- [.js](permuting_two_arrays.js)
- [.py](permuting_two_arrays.py)
- [.rb](permuting_two_arrays.rb)

## Explanation

Given, two arrays, `A` and `B`, we are asked to rearrange the arrays into `A'` and `B'`, such that for every index `i`, `A'[i] + B'[i] >= k`.

You are asked to complete the function `twoArrays`, given `A`, `B`, and `k` as function inputs.

### Visualizing the Prompt

Take the following inputs for example:

- A: `[1,4,5,2,3]`
- B: `[4,2,3,5,1]`
- k: `6`

| i   | A[i] | B[i] | A[i]+B[i] | >=k ? |
| --- | ---- | ---- | --------- | ----- |
| 0   | 1    | 4    | 5         | no    |
| 1   | 4    | 2    | 6         | yes   |
| 2   | 5    | 3    | 8         | yes   |
| 3   | 2    | 5    | 7         | yes   |
| 4   | 3    | 1    | 4         | no    |

The problem asks you to find a solution where `A[i] + B[i] >= k` when `0 <= i < n`. For the above scenario, not all indices `i` satisfy the requirements. Indices `i` of 0 and 4, do not yield a sum that is `>= k`. The prompt asks you to rearrange `A` and `B` such that all indices satisfy the requirements, returning `YES` if it is possible, and `NO` if it is not.

### Code

One way to solve this problem is to sort the arrays, `A` from low to high, and `B` from high to low.

Sorting `A` from low to high yields `[1,2,3,4,5]`

Sorting `B` from high to low yeilds `[5,4,3,2,1]`

| i   | A'[i] | B'[i] | A'[i]+B;[i] | >=k ? |
| --- | ----- | ----- | ----------- | ----- |
| 0   | 1     | 5     | 6           | yes   |
| 1   | 2     | 4     | 6           | yes   |
| 2   | 3     | 3     | 6           | yes   |
| 3   | 4     | 2     | 6           | yes   |
| 4   | 5     | 1     | 6           | yes   |

Then, we loop through each index `i`, and check if the sum of `A'[i]` and `B'[i]` is `>= k`. If, at any index `i`, the sum is not `>= k`, return `NO` immediately.

If each index `i` satisfies the requirements, return `YES`.
