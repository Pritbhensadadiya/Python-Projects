import random

# Easy words list
easy_words = [
    "cat", "dog", "sun", "ball", "tree", "book"
]

# Medium words list
medium_words = [
    "rocket", "guitar", "jungle", "pizza", "camera", "school"
    
]

# Hard words list
hard_words = [
    "microscope", "avalanche", "labyrinth", "oxygen", "pyramid"]

print("WELCOME TO THE PASSWORD GUESSING GAME..")

print("Choose a difficulty level: easy, medium, or hard ")


level = input("Enter difficulty: ").lower()


if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break

    # Generate hint
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:", hint)

print("GAME OVER")
