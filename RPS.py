#RPS.py
#Name: Daud Daud
#Date:
#Assignment: lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  playAgain = "y"
  while playAgain == "y":
  #Randomly choose the computer between 'R', 'P', or 'S'
   computer = random.choice(['R', 'P', 'S']) 
  #Prompt the user for their RPS selection
   player = input("Pick Rock, Paper, Or Scissors (R,P,S) (Don't forget capilatization!): ")
  #Determine winner and state what happened to the user
  print("computer choose" + computer)
  print("player choose" + player)
  if player == "R" and computer == "S":
    print("player wins!")
    wins = wins + 1
  if player == "R" and computer == "P":
    print("computer wins!")
    losses = losses + 1
  if player == "R" and computer == "R": 
    print("Tie!")
    ties= ties + 1
  if player == "P" and computer == "R":
    print("palyer wins!")
    wins = wins + 1
  if player == "P" and computer == "S": 
    print("computer wins!")
    wins= wins + 1
  if player == "P" and computer == "P":
    print("Tie!")
    ties = ties + 1
  if player == "S" and computer == "P":
    print("Player wins!") 
    wins = wins + 1
  if player == "S" and computer == "R":
    print("Computer wins!")
    losses = losses + 1
    if player == "S" and computer == "S":
      print("Tie!")
      ties = ties + 1

   
  

  #Ask the user if they would like to play again.
  playAgain = input("Would you like to play again? (y/n): ")
  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
