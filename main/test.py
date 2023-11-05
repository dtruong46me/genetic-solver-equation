def float_to_binary(value):
    if value == 0.0:
        return "0" * 32

    sign_bit = "0" if value >= 0 else "1"
    value = abs(value)

    # Handle special cases for infinity and NaN
    if value == float('inf'):
        return sign_bit + "1" * 8 + "0" * 23
    if value != value:  # Check for NaN
        return sign_bit + "1" * 8 + "1" + "0" * 22

    # Convert the value to its binary representation
    binary = []
    integer_part = int(value)
    fractional_part = value - integer_part

    # Convert integer part to binary
    while integer_part > 0:
        binary.insert(0, str(integer_part % 2))
        integer_part //= 2

    integer_binary = ''.join(binary)

    # Convert fractional part to binary
    binary = []
    for _ in range(23):
        fractional_part *= 2
        binary.append(str(int(fractional_part)))
        fractional_part -= int(fractional_part)

    fractional_binary = ''.join(binary)

    exponent = len(integer_binary) - 1
    normalized_fraction = integer_binary[1:] + fractional_binary

    # Calculate the exponent and adjust for bias
    exponent_bits = format(exponent + 127, '08b')

    # Combine the sign bit, exponent bits, and fraction bits
    binary_str = sign_bit + exponent_bits + normalized_fraction

    return binary_str


print(-1e3)