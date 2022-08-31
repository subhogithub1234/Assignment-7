n=int(input("Enter the number"))
match n:
    case n if n>0:
        print("Number is positive.")
    case n if n==0:
        print("Number is zero.")
    case n if n<0:
        print("Number is Negative.")
