# Building Simple Calculator using python Project 1

first = input ("Enter First no. : ")
operator = input (" Enter Operator (+,-,*,/,5):")
second = input ("Enter Second no. :")

first = int(first)
second = int(first)

if operator == "+": 
    print ( first + second )
elif operator == "-":
    print (first - second )
elif operator == "*":
    print (first * second )
elif operator == "/":
    print (first / second )
elif operator == "%":
    print (first % second )
else:
    printO("Invalid Operation")

