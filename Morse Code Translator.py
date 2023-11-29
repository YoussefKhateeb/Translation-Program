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
        if char == ' ':
            morse_code += ' '
        elif char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            raise ValueError(f"Invalid character '{char}' in the input. Please enter letters not numbers in the text.")
    return morse_code.strip()

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code == '':
            text += ' '  
        elif code in MORSE_CODE_DICT.values():
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
        else:
            raise ValueError(f"Invalid Morse code '{code}' in the input. Please enter valid Morse code.")
    return text

user_input = input("Enter a English text to translate to Morse Code : ")
try:
    morse_result = text_to_morse(user_input)
    print(f'Text to Morse Code: {morse_result}')
except ValueError as e:
    print(e)

morse_input = input("Enter Morse code for translation: ")
try:
    text_result = morse_to_text(morse_input)
    print(f'Morse Code to Text: {text_result}')
except ValueError as e:
    print(e)
