import random

print("🎲 Welcome to the Guessing Game! 🎲")

print("I'm thinking of a number between 1 and 50... 🤔")


secret = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Take a guess: ")
    if not guess.isdigit():
        print("🚫 Please enter a number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too low! 🐭 Try a bit higher!")
    elif guess > secret:
        print("Too high! 🦒 Maybe lower?")
    else:
        print(f"🎉 Yay! You got it in {attempts} tries! 🏆") 
        break

print("Thanks for playing 💖")

