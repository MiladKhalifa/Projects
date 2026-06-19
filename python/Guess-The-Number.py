import random

print("Welcome to the guessing game!")
while True:
    number = random.randint(1, 100)
    tries = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            tries += 1
        except ValueError:
            print("please type a number!")
            continue

        if guess > number:
            print("Your guess is too high!")
        elif guess < number:
            print("Your guess is too low!")
        else:
            print(f"Congrats you guessed {number} in {tries} tries!")
            break

    while True:
        choice = input("would you like to play again? (y/n): ")
        if choice == "y":
            break
        elif choice =="n":
            exit()
        else:
            print("Please choose (y/n).")