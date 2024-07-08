import random

choices = ["rock", "paper", "scissors"]

def play():
  human_input = input("rock, paper, ya scissor choose karo (r/p/s): ").lower()
  if human_input == 'r':
    human = "rock"
  elif human_input == 'p':
    human = "paper"
  elif human_input == 's':
    human = "scissors"
  else:
    print("Invalid choice. Please select again.")
    return
  
  computer = random.choice(choices)

  print(f"Aapne {human} choose kiya aur Computer ne {computer} kiya")

  if human == computer:
    print("Game tie hogaya")
  elif (human == "rock" and computer == "scissors") or \
       (human == "paper" and computer == "rock") or \
       (human == "scissors" and computer == "paper"):
    print("You win!")
  else:
    print("You lose!")

while True:
  play()
  if input("kya dubaara khelna hai ? (y/n): ").lower() != "y":
    break

print("Khelne k liye thanks")
