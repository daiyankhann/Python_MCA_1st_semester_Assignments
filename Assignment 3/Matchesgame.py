def matchstick_game(predefined_inputs):
    total_matchsticks = 21

    print("Welcome to the Matchstick Game!")
    print("Rules:")
    print("1. There are 21 matchsticks.")
    print("2. You can pick 1, 2, 3, or 4 matchsticks on your turn.")
    print("3. The computer will then pick matchsticks.")
    print("4. Whoever is forced to pick the last matchstick loses the game.")

    input_index = 0

    while total_matchsticks > 1:
       
        try:
            user_pick = int(predefined_inputs[input_index])
            input_index += 1
            print(f"Your turn! You picked {user_pick} matchstick(s).")
        except (ValueError, IndexError):
            print("Invalid input or no more predefined inputs. Game terminated.")
            break

        if user_pick < 1 or user_pick > 4:
            print("Invalid choice! You can only pick 1, 2, 3, or 4 matchsticks.")
            continue

        total_matchsticks -= user_pick

        if total_matchsticks <= 1:
            print("You picked the last matchstick. You lose!")
            break

      
        computer_pick = 5 - user_pick
        print(f"Computer picks {computer_pick} matchstick(s).")
        total_matchsticks -= computer_pick

        if total_matchsticks <= 1:
            print("The computer forces you to pick the last matchstick. You lose!")
            break

        print(f"Matchsticks remaining: {total_matchsticks}")


predefined_inputs = [1, 2, 3, 1]  
matchstick_game(predefined_inputs)