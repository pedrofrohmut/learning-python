# Show the instructions
#
# generate the answer code
#
# game_loop (
#     show(ask_for_guess_message)
#     guess = read_input()
#     numof_guesses + 1
#     game_over = evaluate(guess)
#     if game_over or numof_guesses >= 10
#         break game_loop
#     show(game_state)
# )
#
# game_state { numof_correct_pos, numof_correct_guesses }

import random

COLORS = ["R", "G", "B", "Y",  "W", "O"]
TRIES_LIMIT = 10
ANSWER_LEN = 4

def generate_answer():
    answer = []
    for _ in range(ANSWER_LEN):
        color = random.choice(COLORS)
        answer.append(color)
    return answer


def guess_code():
    # TODO: Fix this crap code
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != ANSWER_LEN:
            print(f"You must guess {ANSWER_LEN} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
            else:
                break
    return guess


def check_answer(guess, answer):
    color_counts = {} # exp: { "G": 2, "R": 1 } means 2 greens and 1 red
    correct_pos_count = 0
    incorrect_pos_count = 0
    # Populate color counts
    for color in answer:
        if color not in color_count:
            color_counts[color] = 0
        color_counts[color] += 1
    # ?
    for g_clr, ans_clr in zip(guess, answer):
        if g_clr == ans_clr:
            correct_pos_count += 1
            color_counts[g_clr] -= 1
    # ?
    for g_clr, ans_clr in zip(guess, answer):
        if g_clr in color_counts and color_counts[g_clr] > 0:
            incorrect_pos += 1
            color_counts[g_clr] -= 1
    return correct_pos_count, incorrect_pos_count


def game():
    print(f"Welcome to mastermind, you have {ANSWER_LEN} to guess the code.")
    print("The valid colors are ", *COLORS)
    answer = generate_answer()
    for i in range(1, TRIES_LIMIT + 1):
        guess = guess_code()
        correct_count, incorrect_count = check_answer(guess, answer)
        if correct_count == ANSWER_LEN:
            print("You cracked the code in {i} tries!")
            break
        print(f"Correct positions: {correct_count} | Incorrect Positions: {incorrect_count}")
    # TODO: Wtf! Else for forloop
    else:
        print("You ran out of tries, the code was: ", *code)

# if __name__ == "__main__":
#     game()


def main():
    game()


main()
