#include <string>

int countingValleys(int steps, string path) {
  bool inMountain = false;
  bool inValley = false;
  int mountains = 0;
  int valleys = 0;
  int elevation = 0;

  for (char p : path) {
    if (p == 'D') {
      if (elevation == 0) {
        inValley = true;
      }
      elevation--;
    }

    if (p == 'U') {
      if (elevation == 0) {
        inMountain = true;
      }
      elevation++;
    }

    if (elevation == 0) {
      if (inMountain) {
        mountains++;
      }
      if (inValley) {
        valleys++;
      }
      inMountain = false;
      inValley = false;
    }
  }

  return valleys;
}
