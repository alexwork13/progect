import random
attemption = 0
rand_number = random.randint(1, 5)

while True:
    intput_number = input("Input number Alena: ")
    attemption += 1
    if intput_number == "stop":
        print("looser")
        break
    elif rand_number == int(intput_number):
        print("You win")
        print(str(attemption) + " - count of attempts")

        break
    elif int(intput_number) > rand_number:
        print ("need less")
    else: print("need more")
