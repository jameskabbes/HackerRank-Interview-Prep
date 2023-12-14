# Plus Minus

## Solutions

- [.js](plus_minus.js)
- [.py](plus_minus.py)
- [.rb](plus_minus.rb)

## Explanation
In this solution, we initalize three varialbes to count the number of positive, negative, and zero values in the array.

Next, we loop through the array, checking whether the item is positive, negative, or zero. After checking, we add 1 count to the appropriate count tracking variable (positive, negative, or zero). 

To calculate the fraction of items that are positive, we take the positive count variable divided by the length of the array. Then, we round the answer to 6 digits. Continue this pattern for the negative, and zero count variables.