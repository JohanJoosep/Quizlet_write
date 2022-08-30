import os               #import operating system for clear()
import pandas as pd     #import pandas librairy as pd 
import time             #import time for sleep()

# assign "df" to the DataFrame created by pd by my csv file
df = pd.read_csv('words.csv')

#to clear the terminal after question was answered
clear = lambda: os.system('cls')

#add a new column named "Times Answered Correctly" and assing all of its rows as 0
df['TAC'] = 0

i = 1
while i <= len(df.TAC) * 2:
    clear()
    #random term that hasnt been answered correctly twice
    from random import randrange
    x = randrange(len(df.TAC))
    while df.TAC[x] == 2:
        x = randrange(len(df.TAC))

    #print term
    print("Term:       " + df.Term[x])  


    #check in user typed the correct definition, print "CORRECT", add 1 to TAC row in df, add one correct answer to i
    if input("Definition: ") == df.Definition[x]:
        print("CORRECT")
        df.TAC[x] += 1
        i += 1
    else:
        #ask user to try again until they get it right
        wrong_input = ""
        while wrong_input != df.Definition[x]:
            print("WRONG " + "correct: " + df.Definition[x])
            time.sleep(3)
            clear()
            print("Term:       " + df.Term[x])
            wrong_input = input("WRONG " + "Try again: ") 
        print("CORRECT")
clear()
print("Everything answered correctly.")