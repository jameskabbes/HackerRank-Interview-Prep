def flippingBits(n)
  # since this is a 32-bit integer, initialize list with 32 bits
  bits = Array.new(32, '0')

  # fill in the end of the bits list with n_as_binary_str
  (0...n_as_binary_str.length).each do |i|
    bits[bits.length - (i + 1)] = n_as_binary_str[n_as_binary_str.length - (i + 1)]
  end

  # swap every bit in list
  bits.each_with_index do |bit, i|
    if bit == '1'
      bits[i] = '0'
    elsif bit == '0'
      bits[i] = '1'
    end
  end

  # turn the bits array into a string, cast it to an int with base 2
  return bits.join('').to_i(2)
end

  end
  