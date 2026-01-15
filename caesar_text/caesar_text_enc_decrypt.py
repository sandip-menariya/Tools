def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # abcdefghijklmnopqrstuvwxyz   --original
    # nopqrstuvwxyzabcdefghijklm   --shifted by 13
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    print(translation_table)
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text=decrypt(encrypted_text,13)
print(decrypted_text)
print(chr(110))

# # full_dot='\u2024'
# full_dot = '●'
# empty_dot = '○'

# strength=4
# intelligence=1
# charisma=2
# st=""
# inte=""
# ch=""
# ans="ren\n"+"STR"+full_dot*strength+empty_dot*(10-strength)+"\n"+"INT"+full_dot*intelligence+empty_dot*(10-intelligence)+"\n"+"CHA"+full_dot*charisma+empty_dot*(10-charisma)
# print(ans)