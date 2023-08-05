import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock','paper','scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices=['rock','paper','scissors']
    return random.choice(choices)

def get_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'draw'
    elif (user_choice=='rock' and computer_choice=="scissors") or (user_choice=='scissors' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='rock'):
        return 'user'
    else:
        return 'computer'

def update_score(winner,scores):
    if winner == 'user':
        scores['user'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    else:
        scores['draw'] += 1
    return scores

def display_score(scores):
    print("Current Score:")
    print(f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}   
    print("Welcome to the Rock paper Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n You Chose: {user_choice}")
        print(f"\n Computer's Choice: {computer_choice}")

        winner = get_winner(user_choice,computer_choice)
        scores = update_score(winner,scores)
        display_score(scores)

        play_again_input = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again_input != 'yes':
            break
    
    print("Thank you for playing Rock, Paper, Scissors with us!")

if __name__ == "__main__":
    main()

