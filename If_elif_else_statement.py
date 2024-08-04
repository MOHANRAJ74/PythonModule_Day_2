#If elif else statement

mark=int(input("Enter Mark: "))

if (mark>=91 and mark<=100):
    print("Grade O")
elif(mark>=81 and mark<=90):
    print("Grade A")
elif(mark>=71 and mark<=80):
    print("Grade B")
elif(mark>=61 and mark<=70):
    print("Grade C")
elif(mark>=51 and mark<=60):
    print("Grade D")
elif(mark>=35 and mark<=50):
    print("Grade E")
elif(mark>=0 and mark<=34):
    print("FAIL")
else:
    print("Invalid Mark")