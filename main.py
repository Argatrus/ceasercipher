"""Encryption and Decryption"""
from nltk.corpus import words
try:
    word_list = words.words()
except KeyError:
    import nltk
    nltk.download('words')
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # noqa  #pylint: disable=line-too-long
LENGTH = len(alphabets)


def ceaser(func: str, scale: int, text: str):
    """Ceaser Cipher"""

    def encrypt(scale: int, text: str):
        """Encryption"""
        encrypted_text = ''
        for letter in text.lower():
            if letter == ' ':
                encrypted_text += ' '
            else:
                for loop in range(LENGTH):
                    if letter == alphabets[loop]:
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
            if letter == ' ':
                decrypted_text += ' '
            else:
                for loop in range(LENGTH):
                    if letter == alphabets[loop]:
                        index = loop-scale
                        break
                decrypted_text += alphabets[index]
        return decrypted_text

    def decrypt_without_scale(text):
        """DECRYPTION BUT WITHOUT SCALE"""
        list_with_answers = []
        for f in range(26):
            list_with_answers.append(decrypt(f, text))
        most_likely_answer = ''
        for decrypted_answer in list_with_answers:
            decrypted_answer = str(decrypted_answer).split(' ')
            for word in decrypted_answer:
                if word in word_list:
                    most_likely_answer += word+' '
            if len(most_likely_answer) > 0:
                break
        list_with_answers.append(f'Most Likely: {most_likely_answer}')
        return list_with_answers

    return decrypt_without_scale(text) if func == 'decrypt' and scale == 0 else encrypt(scale, text) if func == 'encrypt' else decrypt(scale, text) if func == 'decrypt' else None  # noqa  # pylint: disable=line-too-long


print(ceaser('decrypt', 0, 'frpsxwhu vflhqfh'))
