# QUIZ
# Make user answer 5 questions
correct = "Correct"
wrong =  "Wrong Answer"
total_score = []

def quiz():
    print("\n ---Quiz time---!")
    print("Score 4pts or more to pass \n")
    q_1(),q_2(), q_3(), q_4(), q_5(), final_score()
# ======================= Q 1 ==============================
def q_1():
    score = 0
    question = print("What is the capital of Puerto Rico? \n")
    answer = input(" a - Washington DC \n b - San Juan \n c - Milan \n").capitalize()
    if answer == "B":
        score =+ 1
        total_score.append(score)
        print(f"{correct} +{score}= Score {total_score}")
    elif answer == "A" or answer == "C":
        score =+ 0
        total_score.append(score)
        print(f"{wrong} +{score} = Score {total_score}")
    else:
        print("Please try again. Enter valid answer")
        q_1()
# ======================= Q 2 ==============================
def q_2():
    question_2 = print("How do you say 'good evening' in Italian? \n")
    answer = input(" a - Buonasera \n b - Buenas Tardes \n c - Buongiorno \n").capitalize()
    if answer == "A":
        score =+ 1
        total_score.append(score)
        print(f"{correct} +{score}= Score {total_score}")
    elif answer == "B" or answer == "C":
        score =+ 0
        total_score.append(score)
        print(f"{wrong} +{score} =  Score {total_score}")
    else:
        print("Please try again. Enter valid answer")
        q_2()
# ======================= Q 3 ==============================
def q_3():
    question_3 = print("In japanese 'bengoshi' means ? \n")
    answer = input(" a - Water \n b - Lawyer \n c - Train Station  \n").capitalize()
    if  answer == "B":
        score =+ 1
        total_score.append(score)
        print(f"{correct} +{score}= Score {total_score}")
        
    elif answer == "A" or answer == "C":
        score =+ 0
        total_score.append(score)
        print(f"{wrong} +{score} =  Score {total_score}")
    else:
        print("Please try again. Enter valid answer")
        q_3()

# ======================= Q 4 ==============================

def q_4():
    question_4 = print("What does 'como estas?' means in spanish? \n")
    answer = input(" a - What's your name? \n b - I'm hungry? \n c - How are you?  \n").capitalize()
    if answer == "C":
        score =+ 1
        total_score.append(score)
        print(f"{correct} +{score}= Score {total_score}")
    elif answer == "A" or answer == "B":
        score =+ 0
        total_score.append(score)
        print(f"{wrong} +{score} = Score {total_score}")
    else:
        print("Please try again. Enter valid answer")
        q_4()

# ======================= Q 5 ==============================
def q_5():
    question_5 = print("Where is Fairbanks located at? \n")
    answer = input(" a - AK \n b - TN \n c - VT  \n").capitalize()
    if answer == "A":
        score =+ 1
        total_score.append(score)
        print(f"{correct} +{score}= Score {total_score}")
    elif answer == "C" or answer == "B":
        score =+ 0
        total_score.append(score)
        print(f"{wrong} +{score} = Score {total_score}")
    else:
        print("Please try again. Enter valid answer")
        q_5()
            
            
            
## ======================= SCORE ==============================
def final_score():
    while True:
        if len(total_score) == 5:
            result = sum(total_score)
            if result < 4:
                print(f"Score: {result}/5 \n You did not passed , Better Luck Next Time!")
            elif result < 5:
                print(f"Score: {result}/5 \n You passed ,Good Job!")
            else:
                print(f"Score: {result}/5 \n  WOW Perfect Score! ")
            return result
        else:
            print("Invalid answer, Start over again")
            return False
            
    



# Score below 3 pts Fails

# When finish show Score and if Pass or Fails 


quiz()
