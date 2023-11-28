
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.', ' ': '/'}
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char not in MORSE_CODE_DICT:
            raise ValueError(f"Invalid character '{char}' in the input. Please enter letters in the text.")
        elif char == ' ':
            morse_code += '/'
        else:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()  
