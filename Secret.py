import random

secret = random.randint(1, 100)
min_value = 1
max_value = 100
print(secret)
while True:
    guess = input(f"Guess (range {min_value} to {max_value}) ")
    if int(guess) > max_value or int(guess) < min_value:
        print("idiot")
        continue
    if int(guess) == secret:
        print("smart")
        break
    elif int(guess) < secret:
        min_value = int(guess)
    elif int(guess) > secret:
        max_value = int(guess)
