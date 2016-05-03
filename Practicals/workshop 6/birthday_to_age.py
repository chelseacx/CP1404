
def lists_to_dict(list1, list2):
    return dict(zip(list1, list2))

names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

birthdayDictionary = lists_to_dict(names, dobs)

name = input("Please enter a name: ")

while name != "":
    if name not in birthdayDictionary:
        birthday = input("Please enter the date-of-birth in (day/month/year) format: ")
        dob = birthday.split("/")
        birthdayDictionary[name] = dob
    dob = birthdayDictionary[name]
    age = 2016 - int(dob[2])
    print("{} is {} years old".format(name, age))
    name = input("\nPlease enter a name: ")

