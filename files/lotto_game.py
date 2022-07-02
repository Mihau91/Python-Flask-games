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

