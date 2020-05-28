print("Rock..... Paper.. scissors")


player1 = input("Enter player 1's choice:")
player2 = input("Enter player 2's choice:")

if player1 == "rock" and player2 == "scissors":
    print("player1  wins")
elif player1 == "rock" and player2 == "paper":
     print("player2  wins")
elif player1 == "scissors" and player2 == "paper":
     print("player1  wins")
elif player1 == "scissors" and player2 == "rock":
      print("player2  wins")
elif player1 == "scissors" and player2 == "rock":
      print("player2  wins")
elif player1 == "paper" and player2 == "rock":
      print("player1  wins")
elif player1 == "paper" and player2 == "scissors":
      print("player2  wins")

elif player1 == player2:
    print("its a tie")
else:
    print("Something is wrong")
