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
  
    for (let item of appearsOnce) {
      if (!appearsTwice.has(item)) {
        return item;
      }
    }
  }
  