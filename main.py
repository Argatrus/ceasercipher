"""Encryption and Decryption"""
import nltk, time 
from nltk.corpus import words 
try:
    word_list = words.words()
except KeyError:
    nltk.download('words')
    from nltk.corpus import words  
    word_list = words.words()
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # noqa  #pylint: disable=line-too-long

def timerlog(function):
    def wrapper(func: str, scale: int, text: str):
        start = time.time()
        value = function(func, scale, text)
        print(f'Time Taken: {time.time() - start} seconds')
        return value
    return wrapper


@timerlog
def ceaser(func: str, scale: int, text: str):
    """Ceaser Cipher"""

    def encrypt(scale: int, text: str):
        """Encryption"""
        encrypted_text = ''
        for letter in text.lower():
            match letter:
                case ' ':
                    encrypted_text += ' '
                case _:
                    for loop, alphabet in enumerate(alphabets):
                        if letter == alphabet:
                            index = loop+scale
                            break
                    try:
                        encrypted_text += alphabets[index]
                    except IndexError:
                        correct_index = 0
                        for loop in range(scale+1):
                            try:
                                alphabets[correct_index]
                            except IndexError:
                                break
                            correct_index += 1
                            correct_index = scale - correct_index - 1
                        encrypted_text += alphabets[correct_index]
        return encrypted_text

    def decrypt(scale: int, text: str):
        """DECRYPTION"""
        decrypted_text = ''
        for letter in text.lower():
            match letter:
                case ' ':
                    decrypted_text += ' '
                case _:
                    for loop, alphabet in enumerate(alphabets):
                        if letter == alphabet:
                            index = loop-scale
                            break
                    decrypted_text += alphabets[index]
        return decrypted_text.title()

    def decrypt_without_scale(text):
        """DECRYPTION BUT WITHOUT SCALE"""
        list_with_answers = []
        for f in range(26):
            list_with_answers.append(decrypt(f, text))
        most_likely_answer = ''
        for decrypted_answer in list_with_answers:
            decrypted_answer = str(decrypted_answer).split(' ')
            for word in decrypted_answer:
                if word.lower() in word_list:
                    most_likely_answer += word+' '

            index = None
            try:    
                index = list_with_answers.index(most_likely_answer)
            except ValueError:
                pass

            if len(most_likely_answer) > 0:
                break
        list_with_answers.append(f'Most Likely: {most_likely_answer}')
        return f'Most Likely: {most_likely_answer} at index {index}' if most_likely_answer != '' else list_with_answers, list_with_answers

    return decrypt_without_scale(text) if func == 'decrypt' and scale == 0 else encrypt(scale, text) if func == 'encrypt' else decrypt(scale, text) if func == 'decrypt' else None  # noqa  # pylint: disable=line-too-long


print(ceaser('decrypt', 10, 'mywziioi imsoxmo'))