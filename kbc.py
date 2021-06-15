# from typing import SupportsBytes


question_list = [
    "where is pune?",              
    "Where is get-way-of India?",           
    "Who was the first woman Prime Minister of India?",  
    "who is created by python language?",
    "How many union territory of india?",
    "Who invented the Computer?",
    "Who is the largest continent?",
    "Who founded Fecebook?",
    "What is the National Flower of India?",
    "What is the National Bird of India?"
]

options_list = [
  
    ["Maharashtra", "Bangal", "Gujrat", "Bhopal"],   
    ["Chandrapur", "pune", "nagpur", "Delhi"],
    ["Indira Gandhi","Pt.Nehru","Soniya Gandhi","Pratibhatai Patil"],
    ["Albrt ainstrong", "Ramanujam","Grahm bell", "Gudio Van Russam"],
    ["nine", "seven", "eleven", "ten"],
    ["Charlse Babbage","Alexander","Michael","Galileo"],
    ["Urop", "Astreliya", "Ashia", "America"],
    ["Galilio", "Charlse Babbage", "Gudio van russom", "Mark Zuckerberg"],
    ["Rose", "Lotus", "sunflower", "Jasmine"],
    ["parrot", "Peacock", "koyal", "penguins"]
]
solution_list = [1, 4, 1, 4, 1, 1, 3, 4, 2, 2] 
answer=[
    ["(1) Maharastra","(3)Gujrat"],
    ["(1) Chandrapur","(4)Delhi"],
    ["(1) Indira Gandhi","(4) Pratibhatai PAtil"],
    ["(1) Albart ainstrong", "(4) Gudio Van Russam"],
    ["(1) nine", "(2) seven"],
    ["(1) Charlse Babbage", "(4) Galilio"],
    ["(4) America", "(3) Ashia"],
    ["(1) Galilio", "(4) Mark Zuckerberg"],
    ["(1) Rose", "(2) Lotus"],
    ["(2) peacock", "(3) Koyal"]
]

i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    print("\U0001F935")
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a=a+1
    lax=input("do you want to 50 50 lifeline: ")
    if lax=="yes":
        print("accept")
        if count<=1:
            print(answer[b])
            num=input("enter the correct answer: ")
            if num==solution_list[i]:
                s+=1000
                print("your answer is correct")
                print("your win Rs/",a)
                print("\U0001F600") 
            else:
                print("incorrect answer")
                print("you not win Rs/",a)
                print("\U0001F605")
                break
            count+=1
        else:
            print("you already use lifeline: ")
            n=int(input("enter the your answer: "))
            if n==solution_list[i]:
                print("congrat's your answer is right")
                s+=1000
                print("you win Rs/",s)
                print("\U0001F600")
            else:
                print("your answer is wrong")
                print("you win",s)
                print("\U0001F605")
                break
    else:
        pass
    z=int(input("enter your answer: "))
    if z==solution_list[i]:
        print("right answer")
        s+=1000
        print("you win Rs/",s)
        print("\U0001F600")
    else:
        print("no chance")
        print("your answer is wrong")
        print("you win",s)
        print("\U0001F605")
    i=i+1
print("Congragulation.....you are participated in__KBC GAME")
print("You Win Rs/",s)
print("\U0001F947")
print("Thanks for participation")


                








