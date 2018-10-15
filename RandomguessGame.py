import random


n = random.randrange(1, 20, 2)
print("I am thinking of a number between 1 and 20. Take a guess.")

def inputnum():

    a = int(input())
    return a

def GuessGame():
  b = inputnum()

  for i in range(1, 6):

      if n == b:
          print("Good job! You guessed my number in " + str(i) + " guesses!")
          break

      elif ((n-3) <= b and b < n) or (b > n and b <= (n+3)):
            print("Your guess is too high. Take a guess.")
            c = inputnum()

      elif(n != b):
            print("Your guess is too low.")
            c = inputnum()
      b = c
      i+=1



  return


GuessGame()

