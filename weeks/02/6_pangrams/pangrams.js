function pangrams(s) {
  const alphabet = new Set("abcdefghijklmnopqrstuvwxyz");
  const stringSet = new Set(s.toLowerCase());

  for (let letter of alphabet) {
    if (!stringSet.has(letter)) {
      return "not pangram";
    }
  }

  return "pangram";
}
