import random

def main():
  dicerolls = 2
  dicesum = 0
  for i in range(dicerolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dicesum += roll
  print(f'You have rolled a total of {dicesum}')

if __name__== "__main__":
  main()