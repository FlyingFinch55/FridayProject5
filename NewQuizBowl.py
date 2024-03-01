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



#Keep this line for testing becouse I can not spell the answers correctly
#Also making the assumtion that the user will know how to spell correct answers and the full answers 
print(selected_questions)
