__author__ = 'sci-lmw1'

# Programming Language class for CP1404


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"


def test():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    eiffel = ProgrammingLanguage("Eiffel", "Static", True, 1986)

    languages = [ruby, python, vb, eiffel]

    print(eiffel)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    test()