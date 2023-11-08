# Time Conversion

## Solutions
* [.js](time_conversion.js)
* [.py](time_conversion.py)
* [.rb](time_conversion.rb)

## Explanation
To start, it will be handy to have variables designating the `hour`, `minute`, `second`, and `ampm`. Perform basic string slicing to define these.

Generally speaking, this conversion is relatively simple, you add 12 to the `hour` variable if it is after noon (PM). The hour and minute variables do not need to changed.

### Exceptions
However, there are edge cases (noted in the prompt) that preceed this general rule:

#### **12:00:00AM** Midnight: 
This is 00:00:00 in 24-hour format.

To check for this time, we check if the `hour` variable is equal to `12`, and if `ampm` is equal to `'AM'`. When this is the case, set hour equal to the string `'00'`

#### **12:00:00PM** Noon: 
This is 12:00:00 in 24-hour format.

To check for this time, we check if the `hour` variable is equal to `12`, and if `ampm` is equal to `'PM'`. When this is the case, we don't do anything. 

### Generally

For all other times, we simply add `12` to hour variable if ampm is equal to `'PM'`. 

First, we convert our hour variable to an integer. Then we add `12` to the integer. Then, we cast this value back to a string. Now, we would normally have to worry about leading zeroes, `08` instead of `8`, `04` instead of `4`, etc. Since all hours will now be two digits, we don't have to worry about it!

### Finishing up
Finally, print out the `hour`, `minute`, and `second` variables separated by `:`, leaving out the `ampm` variable.
