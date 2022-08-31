print("""
+.Addition
-.Subtraction
*.Multiplication
/. Division""")
ch=input("Enter the choice.")
print("Enter the two numbers:")
x,y=int(input()),int(input())
match ch:
    case '+':
        print("Sum of two numbers:",int((x+y)))
    case '-':
        print("Subtraction of two numbers:",int((x-y)))
    case '*':
        print("Multiplaction of two numbers:",int((x*y)))
    case '/':
        print("Division of two numbers:",float((x/y)))
    case _:
        print("Invalid choice!!!!!")                
