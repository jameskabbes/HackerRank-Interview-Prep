# Breaking the Records

## Solutions

- [.js](breaking_the_records.js)
- [.py](breaking_the_records.py)
- [.rb](breaking_the_records.rb)

## Explanation

### Startup
To start, initialize the `min_score` and `max_score` values equal to the first value of the array. We can safely do this because the array is constrained to have at least one value.

Additionally, set variables `min_score_broken` and `max_score_broken` equal to 0. These will track how many times each "record" is broken. 

### Solving
Loop through the array (skipping the first item) and simultaneously keep track of the `min_score`/`max_score`, and how many times each record has been broken in `min_score_broken`/`max_score_broken`. 

At each item in the array, check if it larger than the current `max_score`. If it is, reset `max_score` as whatever the current item is. Also, add 1 to the `max_score_broken` variable. Similarly, check if the current item is lower than the current `min_score`. If it is, reset the `min_score` as the current item. Add 1 to the `min_score_broken` variable. 

### Return
Finally, return an array containing `[max_score_broken, min_score_broken]`