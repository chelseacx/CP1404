"""
Get into groups of any numbers, solve the following problem.

You are creating a program to calculate the final value of IDD card.
If user top up $5 or $10, the value get added to the card.
If user top up $20, a bonus of $3 get added to the card.
If user top up $50, a bonus of $10 get added to the card.
Your program should contain a menu illustrating the bonus, and print out final value
to the user.
Get user to input current value of card, and the top up value

"""

TWENTY_BONUS = int(3)
FIFTY_BONUS = int(10)

menu = """
You can top up $5, $10, $20 or $50

Bonus:
$3 bonus for $20 top up
$10 bonus for $50 top up

"""
print ("")
print("IDD Card Calculator")
print(menu)

cardValue = float(input("Enter the current value of your card: "))
topUp = int(input("Enter your top up value: "))

if (topUp == 5 or topUp == 10):
    cardValue = cardValue + topUp
elif (topUp == 20):
    cardValue = cardValue + topUp + TWENTY_BONUS
elif (topUp == 50):
    cardValue = cardValue + topUp + FIFTY_BONUS
else:
    print("You have entered an invalid value.")

print("Your new card value is ${:.2f}".format(cardValue))