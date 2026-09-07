# to transition numbers to their corresponding number in alphabet ( 1 => A, 2=> B, 3 => C , ...)                                                                                 
import re

def decode_preserving_characters(input_str):
    def replace_match(match):
        num_str = match.group(0)
        val = int(num_str)

        # Decode if it's within the A-Z alphabet range
        if 1 <= val <= 26:
            return chr(64 + val)

        # Leave the number untouched if it falls outside 1-26
        return num_str

    return re.sub(r"\b\d+\b", replace_match, input_str)


raw_input = input("Write string: " )

# Run the decoder
flag_result = decode_preserving_characters(raw_input)
print(f"Decoded Output: {flag_result}")



