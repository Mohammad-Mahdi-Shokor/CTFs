# a script to decode any string of alphabetical order number ( A => 1 , B => 2, ...)
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

    # Find and process standalone numbers while leaving surrounding characters alone
    return re.sub(r"\b\d+\b", replace_match, input_str)


# Raw input preserving the original symbols and spacing
raw_input = input("Write string: " )

# Run the decoder
flag_result = decode_preserving_characters(raw_input)
print(f"Decoded Output: {flag_result}")
