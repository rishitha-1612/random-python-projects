import random
import re
while(True):
    var_userChoice = input("enter your choice? 'r' for rock, 'p' for paper, 's' for scissor")
    if re.match("[SsRrPp]", var_userChoice):
        print("[R]ock [P]aper [S]cissor")
        print("your input is: "+var_userChoice)
        var_choices=['R','P','S']
        opponentChoice=random.choice(var_choices)
        print("I choose: "+opponentChoice)
        if opponentChoice==str.upper(var_userChoice):
            print("tie")
        elif opponentChoice =="R" and var_userChoice.upper() =="S":
            print("Scissor beats rock i won")
            continue
        elif opponentChoice =="S" and var_userChoice.upper() =="P":
            print("Scissor beats paper i won")
            continue
        elif opponentChoice =="P" and var_userChoice.upper() =="R":
            print("paper beats rock i won")
            continue
        else:
            print("you won")
            continue
    elif re.match("[Qq]", var_userChoice):
        exit()
    else:
        print("invalid input")
        continue