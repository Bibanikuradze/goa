# for ციკლის გამოყენებით 20-ჯერ დაბეჭდეთ თქვენი სახელი და გვარი

for i in range(20):
    print("biba nikuradze")

# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით. იგივე გაიმეორეთ მემეორე ცვლადზე.
# for ციკლით იტერაცია მოახდინეთ დიაპაზონზე, რომლის საწყისი რიცხვია პირველი ცვლადი და საბოლოო რიცხვია მეორე ცვლადი.
# ციკლის ყოველ იტერაციაზე დაბეჭდეთ საიტერაციო ცვლადის კვადრატი

number1 =int(input("enter your number10: "))
number2 =int(input("enter your number20: "))

for i in range(number1, number2):
    print(i**2)


number1, number2 =int(input("enter your number10: ")) (input("enter your number20: "))

for i in range(number1, number2):
    print(i**2)


# Task: Print the Squares of Numbers
# Write a Python program that:
# Asks the user to enter a number 
# 𝑛
# n.
# Uses a for loop to print the square of each number from 1 to 
# 𝑛
# n.

n = int(input("enter number: "))
for i in range(1 , n + 1):
    print(f"The square of {i} is {i**2}")