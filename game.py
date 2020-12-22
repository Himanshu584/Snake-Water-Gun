import random

# variables to store scores
your_score = 0
comp_score = 0

# game loop
while True:
    print("Press 'q' to exit.." )

    # game function to check possibilities
    def game(computer, you):
        if computer == you:
            return None
        else:
            if computer == 's':
                if you == 'w':
                    return False
                elif you == 'g':
                    return True
            if computer == 'w':
                if you == 'g':
                    return False
                elif you == 's':
                    return True
            if computer == 'g':
                if you == 's':
                    return False
                elif you == 'w':
                    return True

    # Generate choices for computer
    computer_val = random.randint(1,3)
    if computer_val == 1:
        computer = 's'
    elif computer_val == 2:
        computer = 'w'
    elif computer_val == 3:
        computer = 'g'

    # Player's Input
    you = str(input("Your Turn: Snake(s), Water(w), Gun(g)::>> "))

    # quit and display score if 'q' pressed
    if you == 'q':
        print(f"Your Score:>> {your_score}")
        print(f"Computer Score:>> {comp_score}")
        break
    elif you != 'q':
        outcomes = ['s', 'w', 'g']
        # check if user input is valid
        if you not in outcomes:
            print("Invalid Selection! Try again")
            you = str(input("Your Turn: Snake(s), Water(w), Gun(g)::>> "))
    
    a = game(computer, you)

    print(f"computer Selected:: {computer}")
    print(f"You Selected:: {you}")

    if a == True:
        print("You win!")
        your_score += 1
    elif a == False:
        print("You loose!")
        comp_score += 1
    else:
        print("Tie!")

    


    

