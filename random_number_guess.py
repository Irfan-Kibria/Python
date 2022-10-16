import random
random_number = random.randint(10,40)
guess = 0

while guess != random_number:
    user_input= int(input("Try your Luck: "))
    if user_input< random_number:
        print("Too Low", user_input)

    elif user_input> random_number:
        print("Too high", user_input)

        continue

    else:
        print("Congratulations, You Won", user_input)

        break

 