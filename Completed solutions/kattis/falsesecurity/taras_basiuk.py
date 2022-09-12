"""
    Solution to the - https://open.kattis.com/problems/falsesecurity
"""
__author__ = "Taras Basiuk"

# Dictionary keeping the mapping between the letters and the "Morse code"
cipherbook = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--',
    ',': '.-.-',
    '.': '---.',
    '?': '----'
}

# We'll need the reverse cipherbook as well
reversed_cipherbook = {}
for k in cipherbook:
    reversed_cipherbook[cipherbook[k]] = k

try: # Caches the EOFError when we read in the entire input file
    while True:
        ciphertext = input().strip() # Read in the ciphertext

        morse_code = [] # List for keeping the Morse code segments
        letter_lenths = [] # List for keeping the lengths of Morse codes

        for c in ciphertext: # For every character in the ciphertext
            morse_code.append(cipherbook[c]) # Store the corresponding Morse code segment
            letter_lenths.append(len(cipherbook[c])) # Store the length of the corresponding Morse code segment

        morse_code = ''.join(morse_code) # Join the segments of the Morse code into one string
        letter_lenths = list(reversed(letter_lenths)) # Reverse the lengths of the Morse code letters
        offset = 0 # Offset where the next Morse code segment of the plaintext begins

        plaintext = [] # List for keeping the plaintext characters
        for ll in letter_lenths: # For every letter Morse code segment length
            # Recover the corresponding plaintext character
            plaintext.append(reversed_cipherbook[morse_code[offset : offset + ll]])
            offset += ll # Update the offset

        print("".join(plaintext)) # Join the characters of the plain text into a single string and print it out
except EOFError:
    # Reached end of file, we're done
    pass
