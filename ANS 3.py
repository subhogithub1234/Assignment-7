print('''--------------------MENU----------------------
a. Check whether a given set of three numbers are lengths of an isosceles
   triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
   angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.''')
x=input("Enter your choice:")
match x:
    case 'c':
        side1=int(input("Enter 1st side:"))
        side2=int(input("Enter 2nd side:"))
        side3=int(input("Enter 3rd side:"))
        if side1==side2 and side2==side3: 
            print("equilateral triangle")
        else:
            print("not equilateral triangle")
    case 'a':
        side1=int(input("Enter 1st side:"))
        side2=int(input("Enter 2nd side:"))
        side3=int(input("Enter 3rd side:"))
        if side1==side2 or side2==side3:
            print("isosceles triangle")
        else:
            print("not isosceles triangle")
    case 'b':
        side1=int(input("Enter 1st side:"))
        side2=int(input("Enter 2nd side:"))
        side3=int(input("Enter 3rd side:"))
        if side1!=side2 and side2!=side3 and side3!=side1:
            print("right triangle")
        else:
            print("not right triangle")
    case 'd':
        exit()
        
            
        

    

