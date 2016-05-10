from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languageList = [ruby, python, vb]

print("The dynamically typed languages are:")
for element in languageList:
    if element.is_dynamic():
        print(element.name)