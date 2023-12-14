# Grading Students

## Solutions

- [.js](grading_students.js)
- [.py](grading_students.py)
- [.rb](grading_students.rb)

## Explanation

In this problem, we are asked to round students' grades according to a certain set of rules. The core logic is contained in the `grade()` function, which takes in a score, and returns a rounded grade. The `gradingStudents()` function loops over the given `grades` array, replacing each item with the rounded value returned from the `grade()` function.

### Grade()

Given a grade, return a rounded grade. Following the recipe defined in the problem, we can create a simple flow.

If the **grade is less that 38**, do not round. Return the original score. Otherwise, continue in the function.

Next, we need to check if the score meets the criteria to be rounded up. To understand the logic, check out the table for the values 81-90.

| Score | Number Mod 5 | To Round | Next Multiple of 5 | Difference |
| ----- | ------------ | -------- | ------------------ | ---------- |
| 81    | 1            | False    | 85                 | 4          |
| 82    | 2            | False    | 85                 | 3          |
| 83    | 3            | True     | 85                 | 2          |
| 84    | 4            | True     | 85                 | 1          |
| 85    | 0            | False    | 90                 | 5          |
| 86    | 1            | False    | 90                 | 4          |
| 87    | 2            | False    | 90                 | 3          |
| 88    | 3            | True     | 90                 | 2          |
| 89    | 4            | True     | 90                 | 1          |
| 90    | 0            | False    | 95                 | 5          |

When the difference between the next multiple of 5 and the score are less than 3, the score should be rounded up to that next multiple of 5. In this case, scores of 83 and 84. We also notice that this corresponds to `Number Mod 5` values of 3 or greater. When `score mod 5 >= 3`, round up. When it is not, return the original score.

To calculate the difference between `score` and the next multiple of 5, we can take `(5-mod)`. Notice for 83, `3+2=5` and for 84, `4+1=5`. Add this difference to the score, and return it.
