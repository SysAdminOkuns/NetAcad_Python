secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess_number = int(input("Guess the secret number: "))

while secret_number:
    if guess_number == secret_number:
        print("Well done, muggle! You are free now.")
        secret_number = 0
    else:
        print("Ha ha! You're stuck in my loop!")