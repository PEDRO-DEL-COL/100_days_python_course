import random

#function to randomize the comkputer's hand
def random_choice():
    random_num = random.randint(0, 2)

    if random_num == 0:
        print("Computer\'s choice:")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        return random_num
    elif random_num == 1:
        print("Computer\'s choice:")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        return random_num
    elif random_num == 2:
        print("Computer\'s choice:")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        return random_num

#welcome
print(''' __          __  _                            _          _____            _        _____                                      _____      _                    _ 
 \ \        / / | |                          | |        |  __ \          | |      |  __ \                                    / ____|    (_)                  | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__) |___   ___| | __   | |__) |_ _ _ __   ___ _ __    ___  _ __  | (___   ___ _ ___  ___  _ __ ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  _  // _ \ / __| |/ /   |  ___/ _` | '_ \ / _ \ '__|  / _ \| '__|  \___ \ / __| / __|/ _ \| '__/ __| |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | \ \ (_) | (__|   < _  | |  | (_| | |_) |  __/ |    | (_) | |     ____) | (__| \__ \ (_) | |  \__ \_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  \_\___/ \___|_|\_( ) |_|   \__,_| .__/ \___|_|     \___/|_|    |_____/ \___|_|___/\___/|_|  |___(_)
                                                                              |/             | |                                                                
                                                                                             |_|                                                                
      ''')

#variable to validade the main loop
quit = False

#main loop
while not quit:

    #creating variable to validate the player's hand
    hand_choice_validator = False

    #loop to validate the hand played
    while not hand_choice_validator:

        player_choice = int(input("Chose:\n1. Rock\n2. Paper\n3.Scisors\n->"))

        if player_choice == 1:
            print('Your choice:')
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            computer_choice = random_choice()
            hand_choice_validator = True
        elif player_choice == 2:
            print('Your choice:')
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            computer_choice = random_choice()
            hand_choice_validator = True
        elif player_choice == 3:
            print('Your choice:')
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            computer_choice = random_choice()
            hand_choice_validator = True
        else:
            print("Please select a valid number.")
            hand_choice_validator = False

    #win or lose conditions
    if player_choice == 1 and computer_choice == 2:
        print("You win!")

    elif player_choice == 2 and computer_choice == 0:
        print("You win!")

    elif player_choice == 3 and computer_choice == 1:
        print("You win!")

    elif player_choice - 1 == computer_choice:
        print("It\'s a tie!")

    else:
        print("You lose!")

    #createing the validation variable
    quit_choice_validator = False

    #loop to check if the user wants to quit or keep playing
    while not quit_choice_validator:
        exit_decision = input("Do you want to keep playing?\n1. Yes\n2. No\n->")

        if exit_decision == "1":
            quit = False
            quit_choice_validator = True
        elif exit_decision == "2":
            quit = True
            quit_choice_validator = True
        else:
            print("Please type a valid choice.")
            quit_choice_validator = False