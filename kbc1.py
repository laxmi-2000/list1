question_list = [ 
    "How many continents are there?",              
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"   
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],

    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

solution_list = [3, 4, 1] 
answer_list=[
    ["(1)four","(3)seven"],
    ["(4)Delhi","(2)Bhopal"],
    ["(4)Agricultue","(1)Software Engineering"]
]
print("kaun Banega codepati (KBC)")
print("\U0001F935")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a=a+1
    num1=input("do you want 50 50 lifeline=")
    if num1=="yes":
        print("accept")
        if count<1:
            print(answer_list[b])
            num2=int(input("enter your answer="))
            if num2==solution_list[i]:
                s+=10000
                print("your answer is correct")
                print("you win Rs/",s)
                print("\U0001F600")
            else:
                print("incorrect answer")
                print("you win Rs/",s)
                print("\U0001F605")
                break
            count+=1
        else:
            print("you already use lifeline")
            m=int(input("enter your answer="))
            if m==solution_list[i]:
                print("congrats, your answer is right")
                s+=10000
                print("you win Rs/",s)
                print("\U0001F600")
            else:
                print("your answer is wrong")
                print("you win",s)
                print("\U0001F602")
                break
    else:
        pass
        k=int(input("enter your answer="))
        if k==solution_list[i]:
            print("right answer")
            s+=10000
            print("you win Rs/",s)
            # print("\U001F600")
        else:
            print("no chance")
            print("your answer is wrong")
            print("you win Rs/",s)
            print("\U0001F62D")
    i=i+1
print("Congragulation.....you are participated in__KBC GAME")
print("You Win Rs/",s)
print("\U0001F947")
print("Thanks for participation")

