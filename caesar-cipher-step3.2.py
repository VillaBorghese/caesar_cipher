alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(in_text, in_shift, in_direction):
    var_text = ""

    if direction == "encode" or direction == "decode":

        if direction == "decode":
            in_shift *= -1

        for i in in_text:
            position_letter = alphabet.index(i)
            shifted_letter = position_letter + in_shift
            # Gestion des cas exceptionnels #
            if shifted_letter > 26:  # cas exceptionnel dépassement alphabet positif
                shifted_letter -= len(alphabet)

            var_text += alphabet[shifted_letter]
    else:
        print("Error please enter a valid command: 'encode' or 'decode'")

    print(f"The {in_direction}d text is {var_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(in_text=text, in_shift=shift, in_direction=direction)
