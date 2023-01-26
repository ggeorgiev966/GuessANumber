import colorama
from colorama import Fore
import random

colorama.init()


def new_game_1():
    computer_number = random.randint(1, 100)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-100): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 100:
            print(Fore.YELLOW + "The number is between 1 and 100.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + "You guessed it!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_1()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            print(Fore.RED + "Too High!")
        else:
            print(Fore.BLUE + "Too Low!")


def new_game_1h():
    player_number_counter = 0
    computer_number = random.randint(1, 100)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-100): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 100:
            print(Fore.YELLOW + "The number is between 1 and 100.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + f"You guessed it on your {player_number_counter} try!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_1h()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            player_number_counter += 1
            print(Fore.RED + f"Too High!")
            print(Fore.RED + f"You have {10 - player_number_counter} tries left!")
        else:
            player_number_counter += 1
            print(Fore.BLUE + f"Too Low!")
            print(Fore.RED + f"You have {10 - player_number_counter} tries left!")
        if player_number_counter == 10:
            print(Fore.RED + f"You lose!")
            print(Fore.RED + f"The number was {computer_number}!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_1h()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue


def new_game_2h():
    player_number_counter = 0
    computer_number = random.randint(1, 1000)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-1000): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 1000:
            print(Fore.YELLOW + "The number is between 1 and 1000.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + f"You guessed it on your {player_number_counter} try!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_1()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            player_number_counter += 1
            print(Fore.RED + f"Too High!")
            print(Fore.RED + f"You have {11 - player_number_counter} tries left!")
        else:
            player_number_counter += 1
            print(Fore.BLUE + f"Too Low!")
            print(Fore.RED + f"You have {11 - player_number_counter} tries left!")
        if player_number_counter == 11:
            print(Fore.RED + f"You lose!")
            print(Fore.RED + f"The number was {computer_number}!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_2h()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue


def new_game_3h():
    player_number_counter = 0
    computer_number = random.randint(1, 10000)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-10000): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 10000:
            print(Fore.YELLOW + "The number is between 1 and 10000.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + f"You guessed it on your {player_number_counter} try!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_1()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            player_number_counter += 1
            print(Fore.RED + f"Too High!")
            print(Fore.RED + f"You have {12 - player_number_counter} tries left!")
        else:
            player_number_counter += 1
            print(Fore.BLUE + f"Too Low!")
            print(Fore.RED + f"You have {12 - player_number_counter} tries left!")
        if player_number_counter == 12:
            print(Fore.RED + f"You lose!")
            print(Fore.RED + f"The number was {computer_number}!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_3h()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue


def new_game_2():
    computer_number = random.randint(1, 1000)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-1000): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 1000:
            print(Fore.YELLOW + "The number is between 1 and 1000.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + "You guessed it!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_2()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            print(Fore.RED + "Too High!")
        else:
            print(Fore.BLUE + "Too Low!")


def new_game_3():
    computer_number = random.randint(1, 10000)
    while True:
        player_input = input(Fore.RESET + "Guess the number (1-10000): ")
        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again!")
            continue
        player_number = int(player_input)
        if 1 > player_number or player_number > 10000:
            print(Fore.YELLOW + "The number is between 1 and 10000.")
            continue
        if player_number == computer_number:
            print(Fore.GREEN + "You guessed it!")
            while True:
                print(Fore.RESET + "Would you like to play again? (Y/N):")
                play_again_response = input()
                accept = ["y", "yes"]
                decline = ["n", "no"]
                if play_again_response.lower() in accept:
                    return new_game_3()
                elif play_again_response.lower() in decline:
                    print("Would you like to return to the start menu? (Y/N):")
                    player_menu_response = input()
                    if player_menu_response.lower() in accept:
                        return game_start()
                    elif player_menu_response.lower() in decline:
                        return SystemExit
                    else:
                        print(Fore.RED + "Invalid input. Try again!")
                        continue
                else:
                    print(Fore.RED + "Invalid input. Try again!")
                    continue
        elif player_number > computer_number:
            print(Fore.RED + "Too High!")
        else:
            print(Fore.BLUE + "Too Low!")


def game_start():
    print(Fore.GREEN + "GUESS THE NUMBER GAME")
    print(Fore.YELLOW + "Choose a game mode:")
    print(Fore.GREEN + "1 - Infinite Tries")
    print(Fore.RED + "2 - Limited Tries")
    valid_game_modes = ["1", "2"]
    game_mode = input(Fore.BLUE + "Game Mode: ")
    while game_mode not in valid_game_modes:
        print(Fore.RED + "Invalid input. Choose again!")
        game_mode = input(Fore.BLUE + "Game Mode: ")
        if game_mode in valid_game_modes:
            break
    if game_mode == "1":
        print(Fore.CYAN + "1 - Easy")
        print(Fore.YELLOW + "2 - Medium")
        print(Fore.RED + "3 - Hard")
        valid_game_difficulty = ["1", "2", "3"]
        game_difficulty = input(Fore.BLUE + "Game Difficulty: ")
        while game_difficulty not in valid_game_difficulty:
            print(Fore.RED + "Invalid input. Choose again!")
            game_difficulty = input(Fore.BLUE + "Difficulty: ")
            if game_difficulty in valid_game_difficulty:
                break
        if game_difficulty == "1":
            return new_game_1()
        elif game_difficulty == "2":
            return new_game_2()
        else:
            return new_game_3()
    if game_mode == "2":
        print(Fore.CYAN + "1 - Easy")
        print(Fore.YELLOW + "2 - Medium")
        print(Fore.RED + "3 - Hard")
        valid_game_difficulty = ["1", "2", "3"]
        game_difficulty = input(Fore.BLUE + "Game Difficulty: ")
        while game_difficulty not in valid_game_difficulty:
            print(Fore.RED + "Invalid input. Choose again!")
            game_difficulty = input(Fore.BLUE + "Game Difficulty: ")
            if game_difficulty in valid_game_difficulty:
                break
        if game_difficulty == "1":
            return new_game_1h()
        elif game_difficulty == "2":
            return new_game_2h()
        else:
            return new_game_3h()


game_start()
