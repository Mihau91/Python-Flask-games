DICE_TYPES = [
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
]


def user_input():
    """
    Function validates user's input and split it into multiplier and modifier
    :return:
    :rtype:
    """
    user_dice = input("Your dice type: ")

    for dice in DICE_TYPES:  # checks each dice type with user input and split it if found one
        if dice in user_dice:
            try:
                multiplier, modifier = user_dice.split(dice)
                return multiplier, modifier
            except ValueError:
                return "Wrong input"
    else:
        return "Wrong input"


def dice_main():
    """
    Main function
    """
    print("Roll the dice game")
    print(user_input())


if __name__ == "__main__":
    dice_main()
