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
    res = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"
    res += "And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!\n".format \
           (animal)
    res += "With a {0}, {0} here and a {0}, {0} there.\n".format(sound)
    res += "Here a {0}, there a {0}, everywhere a {0}, {0}.\n".format(sound)
    res += "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n"
    return res


def main():
    print(song("cow", "moo"))
    print(song("dog", "woof"))
    print(song("cat", "meow"))
    print(song("duck", "quack"))
    print(song("pig", "oink"))


if __name__ == "__main__":
    main()
