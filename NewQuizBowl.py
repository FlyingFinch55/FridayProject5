import sqlite3
import random

conn= sqlite3.connect('FridayProj5.db')
curse = conn.cursor()

# make a question array to store questions and answers as normal strings
questions = []

#getting question and anser from table
cursor = conn.cursor()
cursor.execute("SELECT question, answer FROM QuestAns")
rows = cursor.fetchall()

#filling in the question array with questions and answers gotton from the fetch all
for row in rows:
    questions.append((row[0], row[1]))

# Select 5 random questions for the quiz
selected_questions = random.sample(questions, 5)
#IDK if the use all 10 questions since you gave 10 or 5 since that is what
#the orginal one asked for. so for sake of testing I am doing 5 questions


#Keep this line for testing becouse I can not spell the answers correctly
#Also making the assumtion that the user will know how to spell correct answers and the full answers 
#print(selected_questions)


#A for loop that goes through the 5 random questions
score = 0
for TheQuestion, CorrAnswer in selected_questions:
    print(TheQuestion)
    userAns = input("Your Answer: ")
    if userAns.lower() == CorrAnswer.lower():
        print("Correct!")
        score = score + 1
    if userAns.lower() != CorrAnswer.lower():
        print("Wrong. The correct answer is " + CorrAnswer)

print ("Quiz End. Your score is " + str(score) + "/5")

