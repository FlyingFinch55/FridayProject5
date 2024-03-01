import sqlite3
import random

conn= sqlite3.connect('FridayProj5.db')
curse = conn.cursor()


curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print(curse.fetchall())
print()

curse.execute("SELECT * FROM QuestAns")
print(curse.fetchall())
print()

curse.execute("SELECT question FROM QuestAns WHERE id = 1 ")
print(curse.fetchall())
print()

#Note to self can not do curse.execute("SELECT question for QuestAns WHERE id = var1")
#Where we are using var1 as an incrmentor it does not take the value of var1 just the name
#Also can not compare .fetchall() annsers to strings they are different so always wrong