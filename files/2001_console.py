from random import randint


def dice_roll():
    """
    Function calculates result of the dice throw.

    :return: Result of the throw
    :rtype: int
    """
    result = sum([randint(1, 6) for _ in range(2)])  # calculates throw of two D6 dices.

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

    print("Welcome to 2001 game")
    print(f"Player has: {player_points} points")
    print(f"Computer has: {computer_points} points")
    input("Press Enter to start")

    while player_points < 2001 and computer_points < 2001:
        player_throw = dice_roll()  # roll a dice to get points.
        computer_throw = dice_roll()

        player_points = summary_of_throw(player_points, player_throw)  # using func. to calculate points.
        computer_points = summary_of_throw(computer_points, computer_throw)

        print(f"Player 1 has: {player_points} points \nPlayer 2 has {computer_points} points.")
        input("Press 'Enter'")

    if player_points > computer_points:  # Checks who win
        print("Player wins!")
    elif player_points == computer_points:
        print("Draw!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main_game()
