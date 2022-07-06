from random import randint

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


def dice_throw():
    """
    Function validates user's input and split it into multiplier and modifier
    Calculates dice roll from dice pattern
    :return: dice roll value for proper dice pattern, 'Wrong input' text elsewhere
    :rtype: int, str
    """
    user_dice = input("Your dice type: ").upper()

    for dice in DICE_TYPES:  # checks each dice type with user input and split it if found one
        if dice in user_dice:
            try:
                multiplier, modifier = user_dice.split(
                    dice)  # split and assign 1st part as multiplier and 2nd as modifier
            except ValueError:
                return "Wrong input"
            dice_value = int(dice[1:])  # takes dice value anc cut it to get number
            break
    else:
        return "Wrong input"

    try:
        multiplier = int(multiplier) if multiplier else 1  # set multiplier to 1 if it's empty
    except ValueError:
        return "Wrong input"

    try:
        modifier = int(modifier) if modifier else 0  # set modifier to 0 if it's empty
    except ValueError:
        return "Wrong input"

    result = sum(
        [randint(1, dice_value) for _ in range(multiplier)]) + modifier  # return sum of simulated throw + modifier

    return result


def dice_main():
    """
    Main function
    """
    print("""
    Welcome to Dice Roller where you can simulate throw of different types of dices.
    Explanation:
    
    dice code: xDy + z
    where:
    x - number of dice rolls, if it's 1 you can skip it
    y - dice type e.g. D6, D10
    z - modifier (optional) added to result of throw
    
    Example:
    Dice 2D10+10 means throw of two D10 dices +10 to the result.
    Dice D6 means one throw of D6 dice
    Dice 2D3 means throw of two D3 dices
    
    Possible dices: D3, D4, D6, D8, D10, D12, D20, D100
    """)
    return f"The result is: {dice_throw()}"


if __name__ == "__main__":
    print(dice_main())
