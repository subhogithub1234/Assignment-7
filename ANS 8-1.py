x=input("Enter the 1st string:")
y=input("Enter the 2nd string:")
x1=x.strip()
y1=y.strip()
z=(x1,y1)
match z:
    case z if x1==y1:
        print("String is Identical.")
    case z if x1>y1:
        print("{} is comes after {}".format(x,y))
    
    case z if x1<y1:
        print("{} is comes after {}".format(y,x))    
        
