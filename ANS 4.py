age=int(input("Enter the age:"))
match age:
    
    case age if age in range(1,10):
        print("Kid")
    case age if age in range(10,20):
        print("Teen")
    case age if age in range(20,40):
         print("Young")
    case age if age in range(40,60):
         print("Exprienced")
    case age if age in range(60,200):
         print("Citizen")
    case _:
        print("Invalid choice!!!!")
        
        
