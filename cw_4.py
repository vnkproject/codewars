# Make a program that filters a list of strings and returns a list with only your friends name in it.#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise,
# you can be sure he's not...#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend1(x):
    return [f for f in x if len(f) == 4]

friend2 = lambda x : [f for f in x if len(f) == 4]

if __name__ == "__main__":
    print(friend1(["Ryan", "Kieran", "Jason", "Yous"]))
    print(friend2(["Ryan", "Kieran", "Jason", "Yous"]))