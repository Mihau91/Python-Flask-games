def user_input():
    """
    Takes proper input from a user.
    :return: value provided by user from ["too small", "too big", "you win"]
    :rtype: str
    """
    POSSIBLE_INPUT = ["too small", "too big", "you won"]
    while True:
        user_answer = input().lower()  # lower letters so they can be compered with POSSIBLE_INPUT
        if user_answer in POSSIBLE_INPUT:
            break  # if true get out of the loop
        print("Input is not in 'too small', 'too big', 'you won'")
    return user_answer


user_input()
