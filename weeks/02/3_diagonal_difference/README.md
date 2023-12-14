# Diagonal Difference

## Solutions

- [.js](diagonal_difference.js)
- [.py](diagonal_difference.py)
- [.rb](diagonal_difference.rb)

## Explanation
In this problem, we must do basic calculations on a 2-Dimensional array. We calculate the sum of the numbers in the primary diagonal, the sum of the secondary diagonal, and then take the absolute value of the difference of the two diagonals. This value is then returned.

### 2-D Arrays
`arr`= `[ [1,2,3], [4,5,6], [7,8,9] ]`

Using the example provided, the given 2-D `arr` can be thought of as `[ list0, list1, list2 ]` where:

* `list0` = `[1,2,3]`
* `list1` = `[4,5,6]`
* `list2` = `[7,8,9]`

To access number 6 from `arr`, we would first access `list1` by calling `arr[1]`. To get the number 6 from `list1`, we would call `list1[2]`, since 6 is at index 2. Substituting, we can call `arr[1][2]` to get the value of 6.

### Diagonal Sums
Initialize two variables at zero, `primary_diagonal_sum` and `secondary_diagonal_sum`. The primary diagonal goes from top left to bottom right, the secondary goes from top right to bottom left.

### For Loop
To calculate each diagonal sum, we will use a for loop that loops through indices 0 -> number of rows in `arr`. 

**Primary Diagonal** <br>
The primary diagonal can be modeled by `arr[i][i]` as i loops from 0 to `n_rows - 1`

**1** 2 3 -> `arr[0][0]`<br> 
4 **5** 6 -> `arr[1][1]`<br> 
7 8 **9** -> `arr[2][2]`<br> 

**Secondary Diagonal** <br>
The secondary diagonal can be modeled by `arr[i][n_rows-(i+1)]` as i loops from 0 to `n_rows - 1`

1 2 **3** -> `arr[0][2]`<br> 
4 **5** 6 -> `arr[1][1]`<br> 
**7** 8 9 -> `arr[2][0]`<br> 

As you loop from indices 0 to `n_rows - 1`, keep track of the cumulative sum of the diagonals.

### Returning the Absolute Value of the Difference
Finally, take the difference of the two diagonal sums, and then perform the absolute value operation on that difference. Return the absolute value


