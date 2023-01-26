import random

response = "y"


response=(input("press y to roll the dice and n to exit: "))
while response == "y":
    no=int(random.randint(1,6))
    if no == 1:
        print("[   ]")
        print("[ 0 ]")
        print("[   ]")
    elif no == 2:
        print("[   ]")
        print("[0 0]")
        print("[   ]")
    elif no == 3:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
    elif no == 4:
        print("[0 0]")
        print("[   ]")
        print("[0 0]")
    elif no == 5:
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
    elif no == 6:
        print("[0 0]")
        print("[0 0]")
        print("[0 0]")
    print("\n")