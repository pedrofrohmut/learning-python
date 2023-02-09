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
        code.append(color)
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
