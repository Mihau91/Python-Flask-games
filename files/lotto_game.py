from random import shuffle


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
    print(
        ", ".join((str(number) for number in sorted(numbers))))  # change each int to string in sorted list and print it


def random_numbers():
    """
    Chose 6 numbers from shuffled list

    :return: first 6 numbers of shuffled list
    :rtype: list
    """
    numbers = list(range(1, 49))  # created list of numbers from 1-49
    shuffle(numbers)
    return numbers[:6]  # first 6 el of the list.


def lotto():
    """
    Main function
    """
    user_numbers = get_numbers()  # get list of user numbers
    lotto_numbers = random_numbers()  # get 6 numbers from shuffle list
    hits = 0
    hit_numbers = []

    print("Your numbers: ")
    print_numbers(user_numbers)
    print("Lotto numbers: ")
    print_numbers(lotto_numbers)

    for number in user_numbers:  # checks for each user number if are in lotto numbers
        if number in lotto_numbers:
            hits += 1  # hit's counter
            hit_numbers.append(number)  # added hit numbers to the new list

    if hits > 1:
        print(f"You hit {hits} numbers")
    elif hits == 1:
        print(f"You hit {hits} number")
    else:
        print("No hits. Sorry!")


if __name__ == "__main__":
    lotto()
