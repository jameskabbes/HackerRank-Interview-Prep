function marsExploration(s) {
  const CORRECT_MESSAGE = "SOS";
  let changedLetters = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] !== CORRECT_MESSAGE[i % CORRECT_MESSAGE.length]) {
      changedLetters++;
    }
  }

  return changedLetters;
}
