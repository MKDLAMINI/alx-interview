#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """

    remaining_bytes = 0

    top_bit_mask = 1 << 7
    second_bit_mask = 1 << 6

    for byte in data:

        leading_bit = 1 << 7

        if remaining_bytes == 0:

            while leading_bit & byte:
                remaining_bytes += 1
                leading_bit = leading_bit >> 1

            if remaining_bytes == 0:
                continue

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False

        else:
            if not (byte & top_bit_mask and not (byte & second_bit_mask)):
                return False

        remaining_bytes -= 1

    if remaining_bytes == 0:
        return True

    return False
