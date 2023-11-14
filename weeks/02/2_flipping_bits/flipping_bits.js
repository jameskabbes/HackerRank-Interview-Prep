function flippingBits(n) {
    // turns the integer n into a binary representation of 1's and 0's of the number
    const n_as_binary_str = n.toString(2);
  
    // since this is a 32-bit integer, initialize list with 32 bits
    const bits = Array(32).fill('0');
  
    // fill in the end of the bits list with n_as_binary_str
    for (let i = 0; i < n_as_binary_str.length; i++) {
      bits[bits.length - (i + 1)] = n_as_binary_str[n_as_binary_str.length - (i + 1)];
    }
  
    // swap every bit in list
    for (let i = 0; i < bits.length; i++) {
      if (bits[i] === '1') {
        bits[i] = '0';
      } else if (bits[i] === '0') {
        bits[i] = '1';
      }
    }
  
    // turn the bits array into a string, cast it to an int with base 2
    return parseInt(bits.join(''), 2);
  }
  