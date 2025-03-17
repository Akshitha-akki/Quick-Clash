import random

# This is between computer and User with using random package.

# Game logic
def winner(p1,p2,u1):
    if p1 == p2:
        return "It's a Tie!" 
    elif(p1== "rock" and p2 == "scissor") or (p1== "paper" and p2 == "rock") or (p1== "scissor" and p2 == "paper"):
        return f"{u1} wins!"
    else:
        return "Computer wins!"


def main():
    choiceOne=['rock', 'paper','scissor']
    while True:
        print('----Rock-Paper-Scissor-Game----')
        
        #Entering the user name
        user_1=input('Enter user 1 name: ')
        
        #Making the users to choice from rock, paper, scissor
        playerChoice=input("Choice- rock, paper, scissor: ")
        computerChoice= random.choice(choiceOne)

        # If the user choice is not from the list the it will give error message.
        if (playerChoice not in choiceOne):
            print(f"Invalid input")
        else:
            # print(winner(playerChoice,computerChoice))
            print(f"p1- {playerChoice} and p2- {computerChoice}\n {winner(playerChoice,computerChoice,user_1)}")

        #To know whether players will continue the game or stop.
        play_game=input("Do want to play again (yes/no):")
        if play_game != 'yes':
            break
 
    print('--Thanks for Playing--')
    

if __name__ == "__main__":
    main()

