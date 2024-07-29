print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names = name1 + name2
score = 0
score1 = 0
score2 = 0

score1 += names.lower().count("t")
score1 += names.lower().count("r")
score1 += names.lower().count("u")
score1 += names.lower().count("e")

score2 += names.lower().count("l")
score2 += names.lower().count("o")
score2 += names.lower().count("v")
score2 += names.lower().count("e")

score = str(score1) + str(score2)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

