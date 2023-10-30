import random
from colorama import Fore, Style


def print_game_instructions():
    print("Welcome to Wordle!\nYou have six attempts to guess the Word.\nYour Progress Guide:")
    print(Fore.RED + "A highlighted Red letter indicates that this letter is not in the Word.")
    print(Fore.YELLOW + "A highlighted Yellow letter indicates that this letter is in the Word but not in the correct position.")
    print(Fore.GREEN + "A highlighted Green letter indicates that this letter is in the Word and in the correct position.")


def create_letter_dict(word: str) -> dict:
    count = {}
    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count


def check_guess(secret_word: str, user_guess: str, secret_word_count: dict):
    green = '\x1b[32m'
    orange = '\x1b[33m'
    red = '\x1b[31m'
    colors_list = [None, None, None, None, None]

    for index, letter in enumerate(user_guess):
        if letter in secret_word_count:
            if user_guess[index] == secret_word[index]:
                colors_list[index] = green
                if secret_word_count[letter] == 1:
                    secret_word_count.pop(letter)
                else:
                    secret_word_count[letter] -= 1

    for index, letter in enumerate(user_guess):
        if letter in secret_word_count:
            colors_list[index] = orange
            secret_word_count[letter] -= 1

        else:
            if colors_list[index] is None:
                colors_list[index] = red

    print(f'{colors_list[0]}{user_guess[0]} {colors_list[1]}{user_guess[1]} {colors_list[2]}{user_guess[2]} {colors_list[3]}{user_guess[3]} {colors_list[4]}{user_guess[4]}')


def secret_word_from_file(file_path):
    with open(file_path) as my_file:
        secret_words = my_file.read().splitlines()
        secret_word = random.choice(secret_words)
        return secret_word


def run_game():
    play_again = 'Y'

    while play_again.upper() == 'Y':
        print_game_instructions()
        secret_word = secret_word_from_file('words.txt')
        secret_word_count = create_letter_dict(secret_word)
        tries = 6
        for i in range(tries):
            make_a_guess_prompt = "\nGuess a five letter Word: "
            user_guess = input(Style.RESET_ALL + make_a_guess_prompt)
            while len(user_guess) != 5:
                print(Fore.RED + "Please enter a five letter word!")
                user_guess = input(Style.RESET_ALL + make_a_guess_prompt)

            user_guess = user_guess.upper()
            if user_guess == secret_word:
                print('You have guessed the correct Word!')
                print(Fore.GREEN + user_guess)
                break
            else:
                check_guess(secret_word, user_guess, secret_word_count.copy())
                tries -= 1
                print(Style.RESET_ALL + f"\nYou have {tries} attempt(s) left!")

        play_again = input(Style.RESET_ALL + "\nWould you like to play again? Y/N\n")

    print("\nThanks for playing!")


def main():
    run_game()


if __name__ == "__main__":
    main()




