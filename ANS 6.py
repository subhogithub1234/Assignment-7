s=input("Enter the string:")
x=s.strip()
match x:
    case x if ' ' in x:
        print("The string is multiword string.")
    case x if ' ' not in x:
        print("The string is not multiword string.")
        
