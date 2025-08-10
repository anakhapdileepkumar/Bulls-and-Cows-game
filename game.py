import random

# Generate 4-digit number from 1-9 without repetition
digits = random.sample(range(1, 10), 4)
number = ''.join(map(str, digits))

while True:
    guess = input("Enter your 4-digit guess (digits 1-9, no repeats): ")

    # Check guess validity
    if not guess.isdigit() or len(guess) != 4 or '0' in guess or len(set(guess)) != 4:
        print("Invalid guess. Try again!")
        continue

    # Win condition
    if guess == number:
        print("You win! The number was", number)
        break

    # Count bulls and cows
    bulls = sum(guess[i] == number[i] for i in range(4))
    cows = sum(g in number for g in guess) - bulls

    print(f"{bulls} Bulls, {cows} Cows")
