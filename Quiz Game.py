print("Welcome to FRIENDS Quiz Game!!")
playing = input("Do you want to play my game? ")
if playing.lower() !="yes":
    quit()
print("Okay! Let's play ")
score = 0
answer = input(" Who was Chandler's best friend? ")
if answer.lower() == "joey":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input(" What was the name of Monica's older brother? ")
if answer.lower() == "ross":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input(" What was Chandler Bing's job? ")
if answer.lower() == "no idea":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input(" What was the name of Ross's son? ")
if answer.lower() == "ben":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer = input("Who wrote the song Smelly Cat? ")
if answer.lower() == "pheobe":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print("You got " + str(score) + " questions correct")
