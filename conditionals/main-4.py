#match case method

light = input("Enter the color of light : ")
match light:
    case "green":
        print("Go")
    case "red":
        print("Stop!!")
    case "yellow":
        print("Look!!")
    case _:
        print("Invalid Input")