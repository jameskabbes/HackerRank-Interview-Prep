function lonelyinteger(a) {
    const appearsOnce = new Set();
    const appearsTwice = new Set();
  
    for (let item of a) {
      if (!appearsOnce.has(item)) {
        appearsOnce.add(item);
      } else {
        appearsTwice.add(item);
      }
    }
  
    const difference = new Set([...appearsOnce].filter((x) => !appearsTwice.has(x)));
    const lonely = Array.from(difference)[0];
    return lonely;
} 