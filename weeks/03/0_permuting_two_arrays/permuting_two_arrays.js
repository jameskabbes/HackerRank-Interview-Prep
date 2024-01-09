function twoArrays(k, A, B) {
  A.sort();
  B.sort();
  B.reverse();

  for (let i = 0; i < A.length; i++) {
    if (A[i] + B[i] < k) {
      return "NO";
    }
  }
  return "YES";
}
