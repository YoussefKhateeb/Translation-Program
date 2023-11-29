
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
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in MORSE_CODE_DICT.values():
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
        elif code == '/':
            text += ' '
        else:
            raise ValueError(f"Invalid Morse code '{code}' in the input. Please enter valid Morse code.")
    return text
