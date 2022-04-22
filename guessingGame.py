import random 
print("Number guessing game")

number = random.randint(1,100)

chances = 0
print("Guess a number between a 1 and 100: ")

while chances <= 10:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You won!")

        break
    
    elif guess < number:
        print("Your guess was too low. Guess higher. ", guess)

    else: 
        print("Your guess was too high. Guess lower. ", guess)

    chances += 1
if not chances < 5:
    print("You lose! The number is ", number)
