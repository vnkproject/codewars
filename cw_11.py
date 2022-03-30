# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word
# and an array with words. You should return an array of all the anagrams or an empty array if there are none.

def anagrams(word, words):
    return [w for w in words if sorted(list(word)) == sorted(list(w))]


# def anagrams(word, words):
#     return filter(lambda x: sorted(word) == sorted(x), words)


if __name__ == "__main__":
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))