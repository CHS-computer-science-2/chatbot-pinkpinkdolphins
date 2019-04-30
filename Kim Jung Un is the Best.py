#======= Welcome Message
print("Welcome Comrade to OUR most glorious nation, that being the Democratic People's Republic of Korea,")
print("\nor as the filthy Imperialists call us, North Korea. We the only true legitimate state on the korean penninsula are a bastion of hope and prosperity to the people of Korea.")
print("\nWE are so glad that you have decided to become a part of our great country ruled by the great leader Kim Jung Un,but before we can let you in we'll have to make sure your not a western spy.")
print("\nOur brand new Comrade chat bot 3000 we'll ask you questions to make sure your truley going to be a great north korean citizen")

#Import random and textblob
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from textblob import TextBlob
import random

# Groups of words
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
negativeKeywords = ["america","obama","trump","president","human rights","europe","japan","where's my mom?","internet","south korea", "poverty","seoul","capitalism"]
positiveKeywords = ["dear leader", "Great Leader", "kim", "jong", "un", "il", "sung","russia", "north korea", "communism", "pyongyang"]
questionKeywords = ["who","what","where","when","why","?"]

greetings = ["hello Comrade","hello","greetings"]
comradeGreetings = ["Greetings Peasant!", "Greetings!", "WHAT DO YOU WANT????!!!!", "Go away", "*big sigh* hi"]

#Functions
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def greeting(sentence):
    for words in sentence.split():
        if words.lower() in greetings:
            return(comradeGreetings[random.randint(0,5)])
        else:
            return("TRY AGAIN!!")

#

#Main
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
userInput = input("\n: ")
responce = greeting(userInput)
print("Comrade : " + responce)
