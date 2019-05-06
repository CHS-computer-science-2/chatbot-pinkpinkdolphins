#WELCOME STATEMENT>>>>>>>>>>>>>>>>>>>>>>>
print("Welcome Comrade to OUR most glorious nation, that being the Democratic People's Republic of Korea,")
print("\nor as the filthy Imperialists call us, North Korea. We the only true legitimate state on the korean penninsula are a bastion of hope and prosperity to the people of Korea.")
print("\nWE are so glad that you have decided to become a part of our great country ruled by the great leader Kim Jung Un,but before we can let you in we'll have to make sure your not a western spy.")
print("\nOur brand new Comreade chat bot 3000 we'll ask you questions to make sure your truley going to be a great north korean citizen")

#IMPORTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from textblob import TextBlob
import random

#KEYWORDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
greeting_choice=random.randrange(0,4)
negativeKeywords = ["america","obama","trump","president","human rights","europe","japan","where's my mom?","internet","south korea", "poverty","seoul","capitalism","food","38"]
positiveKeywords = ["dear leader", "Great Leader", "kim", "jong", "un", "il", "sung","russia", "north korea", "communism", "pyongyang","Putin","xi jinping"]
questionKeywords = ["who","what","where","when","why","?"]
greetings=["Hello","What a fine day we are having","Praise our Glorious leader from whom all good in the world stems","Comrade Welcome","Are You a Filthy Capatalist Pig?? We\'ll find out",""]

#DEFINING FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>

#Checking the positive value of a word
def check_positive(userInput):
    positive_amount=0
    userinput=userInput.lower
    for x in userInput:
        if x in positiveKeywords:
            positive_amount+=1
            return positive_amount
# Checking the negative value of a word
def check_negative(userinput):
    negative_amount=0
    userinput=userInput.lower
    for x in userInput:
        if x in positiveKeywords or x in questionKeywords:
            negative_amount+=1
            return negative_amount


#MAIN >>>>>>>>>>>>>>>>>>>
print (greetings[greeting_choice])
userInput = input(":")
