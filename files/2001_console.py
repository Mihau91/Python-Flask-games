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
    Simple function that add points

    :return: sum of points
    :rtype: int
    """
    result = points + to_add
    return result


def main_game():
    """
    Main function with game logic.
    """
    player_1 = 0
    player_2 = 0

    print("Welcome to 2001 game")
    print(f"Player 1 has: {player_1} points")
    print(f"Player 2 has: {player_2} points")
    input("Press Enter to start")

    while player_1 <= 2001 and player_2 <= 2001:
        throw_1 = dice_roll()
        throw_2 = dice_roll()
        player_1 = summary_of_throw(player_1, throw_1)
        player_2 = summary_of_throw(player_2, throw_2)
        print(f"Player 1 has: {player_1} points \nPlayer 2 has {player_2} points.")

    if player_1 > player_2:
        print("Player 1 wins!")
    else:
        print("player 2 wins!")


if __name__ == "__main__":
    main_game()
