alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(in_text, in_shift, in_direction):
    var_text = ""

    # Check if the direction is either 'encode' or 'decode'
    if direction == "encode" or direction == "decode":

        if direction == "decode":

            # If decoding, invert the shift to go backwards in the alphabet
            in_shift *= -1

        # Loop through each character in the input text
        for char in in_text:

            # Check if the character is alphabetic
            if char in alphabet:
                position_letter = alphabet.index(char)
                # Shift the position by the given shift value
                shifted_letter = position_letter + in_shift
                # Handle wrap around if the shifted position exceeds the alphabet length
                if shifted_letter > 26:
                    shifted_letter -= len(alphabet)

                # Add the shifted character to the result string
                var_text += alphabet[shifted_letter]
            else:
                # If the character is not alphabetic, keep it unchanged
                var_text += char

        # Print the result
        print(f"The {in_direction}d text is: '{var_text}'")

    else:
        # If direction is neither 'encode' nor 'decode', prompt the user to enter the correct direction
        print("Error, please enter a valid command: 'encode' or 'decode'")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(in_text=text, in_shift=shift, in_direction=direction)
