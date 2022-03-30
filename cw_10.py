# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

def pig_it(text):
    return ''.join([f'{w[1:]}{w[:1]}ay 'if w.isalpha() else w for w in text.split(' ')]).rstrip()


# import re
# def pig_it(text):
#     return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)


# def pig_it(text):
#     return __import__("re").sub(r'\b\w+\b', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)


if __name__ == "__main__":
    print(pig_it('Pig latin is cool'))
    print(pig_it('O tempora o mores !'))