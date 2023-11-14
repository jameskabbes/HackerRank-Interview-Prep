def flippingBits(n: int) -> int:
    
    # turns the integer n into a binary representation of 1's and 0's of the number
    n_as_binary_str = bin(n)[2:]

    #since this is a 32-bit integer, initialize list with 32 bits
    bits = [ '0', ] * 32

    # fill in the end of the bits list with n_as_binary_str
    for i in range(len( n_as_binary_str )):
        bits[ len(bits)-(i+1) ] = n_as_binary_str[ len(n_as_binary_str)-(i+1) ]

    # swap every bit in list
    for i in range(len(bits)):
        if bits[i] == '1':
            bits[i] = '0'
        elif bits[i] == '0':
            bits[i] = '1'

    # turn the bits list into a string, cast it to an int with base 2
    return int(''.join(bits), 2)

print (flippingBits(12))
    