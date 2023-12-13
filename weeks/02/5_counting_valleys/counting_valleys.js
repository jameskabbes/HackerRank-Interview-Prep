function countingValleys(steps, path) {
  let inMountain = false;
  let inValley = false;
  let mountains = 0;
  let valleys = 0;
  let elevation = 0;

  for (let i = 0; i < path.length; i++) {
    let p = path[i];

    if (p === "D") {
      if (elevation === 0) {
        inValley = true;
      }
      elevation -= 1;
    }

    if (p === "U") {
      if (elevation === 0) {
        inMountain = true;
      }
      elevation += 1;
    }

    if (elevation === 0) {
      if (inMountain) {
        mountains += 1;
      }
      if (inValley) {
        valleys += 1;
      }
      inMountain = false;
      inValley = false;
    }
  }

  return valleys;
}
