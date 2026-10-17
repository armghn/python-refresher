from random import randint


def win(computer_number, guess):
    return computer_number == guess


def get_a_guess():
    n = int(input("Guess a number: "))
    return n


def answer(computer_number, guess):
    if computer_number > guess:
        return "My number is larger!"
    elif computer_number < guess:
        return "My number is smaller!"
    else:
        return "Bingo!"


guess = 0

computer_number = randint(1, 20)

while not win(computer_number, guess):
    guess = get_a_guess()
    print(answer(computer_number, guess))



# while True:
#     n = int(input("Guess the number: "))
#     if n > num:
#         print("My number is smaller!")
#     elif n < num:
#         print("My number is larger!")
#     else:
#         print("Bingo!")
#         break