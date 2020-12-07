
value = input("Please enter a number\n")
a = ["4", "0", "6", "9"]

def count_holes(value):
    holes = 0
    for n in value:
        if n in a:
            holes += 1
        if n in "8":
            holes += 2
    return holes


def check_zero(): 
    if value.startswith(('0')) == False:
       print(count_holes(value))
    else:
       print(count_holes(value) - 1)
    return

if value.isnumeric():
   value = str(value)
   check_zero()
else:
    print("Must be a number")
