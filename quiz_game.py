print("welcome to our quiz game")
answer=input("are u ready to play the quiz (yes/no): ")
score =0
total_questions = 3
if answer.lower() == "yes":
    answer=input("question 1:What kind of fish do penguins catch at night?")
    if answer.lower() =="star fish" or answer.lower() == "starfish":
        score+=1
        print("correct")
    else:
        print("wrong answer, correct answer is 'STAR FISH'")

    answer=input("question 2: Which vegetable has the best kung fu?")
    if answer.lower() =="broc lee" or answer.lower() == "broccoli":
        score+=1
        print("correct")
    else:
        print("wrong answer, correct answer is 'BROC LEE'")

    answer=input("question 2:What's the hardest tea to swallow?")
    if answer.lower() =="reality":
        score+=1
        print("correct")
    else:
        print("wrong answer, correct answer is 'REALITY'")
    print("thankyou for playing the game, you attempted",score,"questions correctly")
else:
    print("okay bye")

    

                 
    