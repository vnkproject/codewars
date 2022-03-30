# In this kata you are required to, given a string, replace every letter with its position in the alphabet.#
# If anything in the text isn't a letter, ignore it and don't return it.#
# "a" = 1, "b" = 2, etc.
def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alphabet.find(s)+1) for s in list(text.lower()) if s in list(alphabet)]).strip()


if __name__ == "__main__":
    text = "The sunset sets at twelve o' clock."
    alphabet_position(text)
