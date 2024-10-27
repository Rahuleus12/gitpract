feedbacks={}
average=0
while(True):
    studentName=input("Enter the name of student: ")
    print(studentName,"please enter your feedback number from 1 to 5")
    number=int(input())
    if(number>5 or number <0):
        print("Only feedback from between 1 and 5 is acceptable please enter your name feedback again")
    else: 
        feedbacks[studentName]=number
    check=input("Has every student given a feedback?(y/n)")
    if(check == 'y'):
        break
    else:
        continue
for key,value in feedbacks.items():
    average=average+value
average=average/len(feedbacks)
match average:
    case(5):
        print("Excellent")
    case(4):
        print("good")
    case(3):
        print("average")
    case(2):
        print("not good")
    case(1):
        print("replace")
    case(0):
        print("Replace now")