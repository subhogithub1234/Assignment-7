n=int(input("Enter the number:"))
match n:
    case n if n%2==0 and  n/10 <0:
         print("Prateek Jain")  
    case n if n%2==0:
        print("Saurabh Shukla.")
    case n if n%2!=0:
        print("Aditya Choudhary.")
    case _:
        print("Invalid choice!!!")
