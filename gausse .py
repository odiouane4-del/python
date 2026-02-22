secret_number = 7 
guess = int(input("Guess the number: "))
cose = 0
limit = 5
while guess != secret_number and cose < limit:
 guess = int(input("Guess the number: "))
 cose += 1
 if guess == secret_number:
    print("Congratulations! You guessed the number.")
 elif guess < secret_number:
    print("Too low! Try again.")
 elif guess > secret_number:
      print("Too high! Try again.")
if cose == limit:
    print("Sorry, you have reached the maximum number of guesses.")