#built in function
print("abc")
int("4")

#create a new function
def print_food(num_of_fries, num_of_cookies):
    calories_fries = 100
    calories_cookies = 70

    total_fries_calories = calories_fries * num_of_fries
    total_cookies_calories = calories_cookies * num_of_cookies
    total_calories = total_fries_calories + total_cookies_calories

    print("The total calories is {:d}.".format(total_calories))

print_food(2,3)
