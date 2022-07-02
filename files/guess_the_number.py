from random import randint


def get_number():
    """
    Chcecks if given number is int.
    Try until user gives proper number.

    :return: given number as int
    :rtype: int
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("Wrong input! Type only integer number!")

    return result


def guess_the_number():
    """
    Main function
    """
    print("""Welcome to "Guess The Number" game. Your task is to guess the number from 1 - 100. Good luck!""")
    given_number = get_number()
    secret_number = randint(1, 100)

    while given_number != secret_number:
        if given_number < secret_number:
            print("Your number is too small. Try again.")
        else:
            print("Your number is too big. Try again.")
        given_number = get_number()
    print("Congratulations! You win!")


if __name__ == '__main__':
    guess_the_number()
