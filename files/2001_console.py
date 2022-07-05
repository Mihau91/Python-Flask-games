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


def dice_roll(dice_type1, dice_type2):
    """
    Function takes input from user, checks type of dice and calculates result of the dice throw.

    :return: Result of the throw
    :rtype: int
    """
    for dice in DICE_TYPES:  # checks each dice type with user input and takes the value.
        if dice in dice_type1:
            dice_value1 = int(dice[1:])  # takes dice value anc cut it to get number

    for dice in DICE_TYPES:
        if dice in dice_type2:
            dice_value2 = int(dice[1:])


    result = sum([randint(1, dice_value1) + randint(1, dice_value2)])  # calculates throw of two D6 dices.

    return result


def summary_of_throw(points, to_add):
    """
    Function calculates point depends on throw.

    :return: calculated points
    :rtype: int
    """
    if to_add == 7:  # if statements to properly add point according to game's rules.
        result = points // 7
    elif to_add == 11:
        result = points * 11
    else:
        result = points + to_add

    if result > 2001:  # to prevent exceeding points over 2001
        result = 2001

    return result


def main_game():
    """
    Main function with game logic.
    """
    player_points = 0
    computer_points = 0

    print("""
    Welcome to 2001 game.
    Rules are simple. Both opponents have to throw two D6 dices.
    First who collect 2001 win, but if player hits 7 on dices needs to divide score by 7,
    if player hits 11 on dices needs to multiple score by 11. Good luck!
    -------------------------------------------------------------------------------------
    """)

    print(f"Player has: {player_points} points")
    print(f"Computer has: {computer_points} points")
    input("Press Enter to start")

    while player_points < 2001 and computer_points < 2001:
        player_throw = dice_roll("D6", "D6")  # roll a dice to get points.
        computer_throw = dice_roll("D6", "D6")

        player_points = summary_of_throw(player_points, player_throw)  # using func. to calculate points.
        computer_points = summary_of_throw(computer_points, computer_throw)

        print(f"Your throw: {player_throw}\nComputer's throw: {computer_throw}\n")
        print(f"Player has: {player_points} points \nComputer has {computer_points} points.")
        input("Press 'Enter'")
        print("----------------------")

    if player_points > computer_points:  # Checks who win and prints it.
        print("Player wins!")
    elif player_points == computer_points:
        print("Draw!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main_game()
