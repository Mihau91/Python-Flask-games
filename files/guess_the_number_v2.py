def user_input():
    """
    Takes proper input from a user.
    :return: value provided by user from ["too small", "too big", "you win"]
    :rtype: str
    """
    POSSIBLE_INPUT = ["too small", "too big", "you win"]
    while True:
        user_answer = input().lower()  # lower letters, so they can be compared with POSSIBLE_INPUT
        if user_answer in POSSIBLE_INPUT:
            break  # if true get out of the loop
        print("Input is not in 'too small', 'too big', 'you win'")
    return user_answer


def guess_the_number():
    """
    Main function
    """
    print("""
    Welcome to Guess The Number game 
    where this time it's computer's turn to guees your number!
    Imagine number between 0 and 1000! 
    After given answer by computer type 'too small', 'too big' or 'you win""")
    print("Press 'Enter' to continue")
    input()

    min_number = 0
    max_number = 1000
    user_answer = ""

    while user_answer != "you win":
        guess = (max_number - min_number) // 2 + min_number  # calculate guess number
        print(f"Your number is: {guess}")
        user_answer = user_input()  # user input (too small/too big/you win)
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess

    print("Hurra! I guess!")



if __name__ == "__main__":
    guess_the_number()
