"""
Coding practice -- Module 3
10. Lyrics
Write a program to print the lyrics of the song "Old MacDonald." Your program
should print the lyrics for five different animals (five verses), similar to
the example verse below:

Old MacDonald had a farm, ee-igh, ee-igh, oh!
And on that farm he had a cow, ee-igh, ee-igh, oh!
With a moo, moo here and a moo, moo there.
Here a moo, there a moo, everywhere a moo, moo.
Old MacDonald had a farm, ee-igh, ee-igh, oh!

"""


def song(animal, sound):
    # method 1
    res = """Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
And on that farm he had a {n}, Ee-igh, Ee-igh, Oh!
With a {s}, {s} here and a {s}, {s} there.
Here a {s}, there a {s}, everywhere a {s}, {s}.
Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n""".format(n = animal, s = sound)\


    # method 2
    c = """
Old MacDonald had a farm, ee-igh, ee-igh, oh!
And on that farm he had a cow, ee-igh, ee-igh, oh!
With a moo, moo here and a moo, moo there.
Here a moo, there a moo, everywhere a moo, moo.
Old MacDonald had a farm, ee-igh, ee-igh, oh!"""
    return c.replace("cow", animal).replace("moo", sound)


    # method 3
    res = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n" + \
          "And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!\n".format(animal) + \
          "With a {0}, {0} here and a {0}, {0} there.\n".format(sound) + \
          "Here a {0}, there a {0}, everywhere a {0}, {0}.\n".format(sound) + \
          "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n" 
    return res


def main():
    print(song("cow", "moo"))
    print(song("dog", "woof"))
    print(song("cat", "meow"))
    print(song("duck", "quack"))
    print(song("pig", "oink"))


if __name__ == "__main__":
    main()
