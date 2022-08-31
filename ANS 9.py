x=int(input("Enter the year"))
match x:
    case x if x%400==0 and  x%4==0:
        print("Century leapyear.")
    case x if x%100==0 and  x%400!=0:
         print("Century but not leapyear.")
    case x if x%4==0 and  x!=400:
        print("Leapyear but not Century.")
        
        
