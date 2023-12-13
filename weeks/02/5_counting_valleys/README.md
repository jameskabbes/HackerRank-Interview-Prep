# Counting Valleys

## Solutions

- [.cpp](counting_valleys.cpp)
- [.js](counting_valleys.js)
- [.py](counting_valleys.py)
- [.rb](counting_valleys.rb)

## Explanation

At each step in the path, we **start by checking if the step is uphill or downhill**.

Once we decide whether we are heading uphill or downhill, we need to check if our current elevation is at 0. This is significant since mountains and valleys both begin at sea level. If we are currently at sea level (elevation of 0), stepping uphill means we are starting a new mountain, while stepping downhill means we are starting a new valley. Update `inMountain` and `inValley` accordingly. Finally, when stepping up, increase the elevation by 1. And when stepping down, decrease the elevation by 1.

**After processing the elevation change given the step direction**, we need to check if we are back at sea level. Ending up at sea level is significant because it signifies the end of both mountains and valleys.

If we end up at sea level after stepping, we come to the end of our mountain or valley. If we were just `inMountain`, we increment `mountains` by 1. If we were just `inValley`, we increment `valleys` by 1. Finally, reset `inMountain` and `inValley` to `False`, since being at sea level singifies the end of both.

**note**: Alternatively to keeping track of `inMountain` and `inValley`, you could just access the last step taken to get to sea level. If you stepped down to get to sea level, you were just in a mountain. If you stepped up to get to sea level, you were just in a valley.
