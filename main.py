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

for word in prompt:
    word=word.replace("!","").replace("'","").replace(".","")
    if word in positive_words:
        total_score+=1
    elif word in negative_words:
        total_score-=1

if total_score>0:
    print("Positive")
elif total_score<0:
    print("Negative")
else:
    print("Neutral")