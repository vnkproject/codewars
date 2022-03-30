# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
# letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
# "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    print(" ".join([s[::-1] if len(s) > 4 else s for s in sentence.split(" ")]))


if __name__ == "__main__":
    sentences1 = "Welcome"
    sentences2 = "Hey fellow warriors"
    spin_words(sentences1)
    spin_words(sentences2)
