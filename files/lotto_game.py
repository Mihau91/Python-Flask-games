from random import randint


def get_number():
    """
    Get number from user
    :return: given number
    :rtype: int
    """
    while True:
        try:
            user_num = int(input("Chose the number: "))
            break
        except ValueError:
            print("Wrong input! Type only integer number")
    return user_num


def get_numbers():
    """
    Get 6 numbers from users that are in range of 1 - 49

    :return: list of numbers
    :rtype: list
    """
    user_numbers = []
    while len(user_numbers) < 6:
        number = get_number()
        if number not in user_numbers and 0 < number <= 49:
            user_numbers.append(number)
        else:
            print("Same number or number over the range 1 - 49!")

    return user_numbers


def print_numbers(numbers):
    """
    Print given numbers with ascending order.

    :param numbers: list of numbers
    :type numbers: list
    """
    print(", ".join((str(number) for number in sorted(numbers))))


def lotto():
    """
    Main function
    """
    print_numbers(get_numbers())


if __name__ == "__main__":
    lotto()
