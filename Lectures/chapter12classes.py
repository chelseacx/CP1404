#
# class Fruit:
#
#     def __init__(self, name="", color=""):
#         self.name = name    # self.name means the attribute name belongs to class fruit
#         self.color = color
#         self.__waterContent = "" #private variable
#
#     def __str__(self):
#         return "Fruit name: {}; Fruit color: {}; ".format(self.name, self.color)
#
#     def eat(self):
#         print("Eating fruit")
#
#
# class AsianFruit(Fruit):
#     """
#     AsianFruit class inherits from Fruit
#     """
#     def __init__(self):
#         self.name = "AsianFruit"
#
#
# def main():
#
#     papaya = AsianFruit()
#     print(papaya) #calling the superclass method
#
#     # mango = Fruit()
#     # print(mango)
#     # strawberry = Fruit("Fruit1", "red")
#     # print(strawberry)
#
#
# main()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

point1 = Point(10,90)
print (point1)



