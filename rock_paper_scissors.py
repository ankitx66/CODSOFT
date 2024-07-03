import random

choices = ["rock", "paper", "scissors"]

def play():
  human = input("rock, paper, ya scissor choose karo (r/p/s): ")
  computer = random.choice(choices)

  print(f"Aapne {human} choose kiya aur Computer ne {computer} kiya")

  if human == computer:
    print("Game tie hogaya")
  elif (human == "r" and computer == "s") or \
       (human == "p" and computer == "r") or \
       (human == "s" and computer == "p"):
    print("You win!")
  else:
    print("You lose!")

while True:
  play()
  if input("kya dubaara khelna hai ? (y/n): ") != "y":
    break

print("Khelne k liye thanks")
