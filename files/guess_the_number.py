from random import randint


def get_number():
    """
    Chcecks if given number is int.
    Try until user gives proper number.

    :return: given number as int
    :rtype: int
    """
    result = int(input("Guess the number: "))
    return result


def guess_the_number():
    """
    Main function
    """
    print("""Welcome to "Guess The Number" game. Your task is to guess the number from 1 - 100. Good luck!""")
    given_number = get_number()
    secret_number = randint(1, 100)
    if given_number == secret_number:
        print("You win!")
    elif given_number < secret_number:
        print("Your number is too small. Try again.")
    else:
        print("Your number is too big. Try again.")


if __name__ == '__main__':
    guess_the_number()
