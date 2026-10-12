from random import randint


def win(computer_number, guess):
    return computer_number == guess


def get_a_guess():
    n = int(input("Guess a number: "))
    return n


def answer(computer_number, guess):
    if computer_number > guess:
        return "My number is larger!"
    if computer_number < guess:
        return "My number is smaller!"
    return "Bingo!"


def finish(num, count, best_player):
    print(f"My number was {num} and you found it in {count} guess(es)!")
    if best_player != 0:
        print(f"And the best player found it in {best_player} guess(es)!")
    answer = input("Do you want to play again? (Y/N) ")
    if answer.lower() == 'y':
        return True
    return False


play_again = True

best_player = 0

while play_again:
    guess = 0

    computer_number = randint(1, 20)

    count = 0
    while not win(computer_number, guess):
        count += 1
        guess = get_a_guess()
        print(answer(computer_number, guess))

    if best_player == 0 or count < best_player:
        best_player = count
    play_again = finish(computer_number, count, best_player)






# while True:
#     n = int(input("Guess the number: "))
#     if n > num:
#         print("My number is smaller!")
#     elif n < num:
#         print("My number is larger!")
#     else:
#         print("Bingo!")
#         break