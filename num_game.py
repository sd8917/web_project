import  random
computer_guess = random.randint(0,6)

while True:
    user_input = int(input("enter the number btw 0 to 6 : "))
    if user_input == computer_guess:
        print("!!GAME OVER")
        print("You Win")
        break
    if computer_guess > user_input:
        print("The valur is smaller type big value")
    else:
        print("THE value is greater type smaller value")
