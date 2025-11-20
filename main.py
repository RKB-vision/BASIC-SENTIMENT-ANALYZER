#CODE HERE😌
from turtle import pos


positive_words=set()
negative_words=set()

with open("positive words.txt","r") as file:
    for word in file:
        positive_words.add(word.strip())

with open("negative words.txt","r") as file:
    for word in file:
        negative_words.add(word.strip())

total_score=0

print("------Welcome to Sentiment Analyzer(o1)------")

prompt=input("Enter the comment").lower().split()

adjust=[]

for word in prompt:
    word=word.replace("!","").replace("'","").replace(".","")
    if word.isalpha():
        adjust.append(word)
        if word in positive_words:
            total_score+=1
        elif word in negative_words:
            total_score-=1

if len(adjust)>100:
    if total_score>5:
        print("Positive")
    elif total_score<-5:
        print("Negative")
    else:
        print("Neutral")
else:
    if total_score>0:
        print("Positive")
    elif total_score<0:
        print("Negative")
    else:
        print("Neutral")