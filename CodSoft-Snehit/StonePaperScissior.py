import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def print_scores(user_score, computer_score):
    print("User Score:", user_score)
    print("Computer Score:", computer_score)

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print_scores(user_score, computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()