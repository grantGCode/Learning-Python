from random import choice

capital = "Austin"

bird = "Mockingbird"

flower = "Bluebonnet"

song = "Texas, Our Texas"


def randomfunfact():
    funfacts = [
        "Texas’ name comes from a Caddo Indian word, “teycha,” which translates to friends or allies.",
        "Austin, Texas’ largest city, is known as the “live music capital of the world,” boasting several major festivals like South by Southwest and Austin City Limits.",
        "Texas Was Once An Independent Nation.",
        "Dr. Pepper Was Invented in Texas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()
# The if statement will run the randomfunfact() function when the module is ran or it is the main file.

# randomfunfact()
# If I were to just call randomfunfact() the function will run every time it is imported into another .py file and that external file is ran.