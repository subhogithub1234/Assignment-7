x=input("Enter your favourit colour:")
y=["yellow","blue","orange","white","black","red"]

for colour in y:
    if colour in x:
        c=colour
        break
else:
    c="other"

match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
        
