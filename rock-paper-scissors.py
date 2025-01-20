import random

user_score = 0
computer_score = 0
print("\n==== Rock, Paper, Scissors: Best of 5 Game ====")

while user_score < 3 and computer_score < 3:
    user = input("\nChoose your weapon (rock, paper, scissors): \n").lower()
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        print(f"Both players chose {user}. It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        print(f"Computer chose {computer} and you chose {user} You win!")
        user_score += 1
    else:
        print(f"Computer chose {computer} and you chose {user}. You lose.")
        computer_score += 1
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

if user_score > computer_score:
    print("\nCongratulations! You won the game!\n")
else:
    print("\nOh no, computer won the game - better luck next time!\n")

    