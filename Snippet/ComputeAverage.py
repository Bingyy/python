 1  # Prompt the user to enter three numbers
2 number1 = eval(input("Enter the first number: "))
3 number2 = eval(input("Enter the second number: "))
4 number3 = eval(input("Enter the third number: "))
5
6 # Compute average
7 average = (number1 + number2 + number3) / 3 8
9 # Display result
10 print("The average of", number1, number2, number3, 11 "is", average)