print("Choose your Category")
print("       ")
print("1. Country")
print("2. Animals")
print("3. Food")
print("       ")

choice = input("Enter your Choice: ")

if choice == '1':
    print("Country")
    p1 = input("Enter Name of the Country: ")
    l1 = len(p1)
    p2 = input("Enter Name of the Country: ")
    l2 = len(p2)
    p3 = input("Enter Name of the Country: ")
    l3 = len(p3)
    p4 = input("Enter Name of the Country: ")
    l4 = len(p4)
    if l1 > l2 and l1 > l3 and l1 > l4:
        print("Player 1 is the Winner!")
    elif l2 > l1 and l2 > l3 and l2 > l4:
        print("PLayer 2 is the Winner!")
    elif l3 > l1 and l3 > l2 and l3 > l4:
        print("Player 3 is the Winner!")
    elif l4 > l1 and l4 > l2 and l4 > l3:
        print("Player 4 is the Winner!")
    else:
        print("Multiple Players Draw")
        exit()

print("            ")
print("Choose your Category")
print("            ")
print("1. Animals")
print("2. Food")

choice = input("Enter your Choice")

if choice == '1':
    print("Animals")
    p1 = input("Enter Name of the Animals: ")
    l1 = len(p1)
    p2 = input("Enter Name of the Animals: ")
    l2 = len(p2)
    p3 = input("Enter Name of the Animals: ")
    l3 = len(p3)
    p4 = input("Enter Name of the Animals: ")
    l4 = len(p4)
    if l1 > l2 and l1 > l3 and l1 > l4:
        print("Player 1 is the Winner!")
    elif l2 > l1 and l2 > l3 and l2 > l4:
        print("PLayer 2 is the Winner!")
    elif l3 > l1 and l3 > l2 and l3 > l4:
        print("Player 3 is the Winner!")
    elif l4 > l1 and l4 > l2 and l4 > l3:
        print("Player 4 is the Winner!")
    else:
        print("Multiple Players Draw")
        exit()

print("Choose your Category")
print("               ")
print("1. Food")
print("               ")

choice = input("Enter your Choice")

if choice == '1':
    print("Food")
    p1 = input("Enter Name of the Food: ")
    l1 = len(p1)
    p2 = input("Enter Name of the Food: ")
    l2 = len(p2)
    p3 = input("Enter Name of the Food: ")
    l3 = len(p3)
    p4 = input("Enter Name of the Food: ")
    l4 = len(p4)
    if l1 > l2 and l1 > l3 and l1 > l4:
        print("Player 1 is the Winner!")
    elif l2 > l1 and l2 > l3 and l2 > l4:
        print("PLayer 2 is the Winner!")
    elif l3 > l1 and l3 > l2 and l3 > l4:
        print("Player 3 is the Winner!")
    elif l4 > l1 and l4 > l2 and l4 > l3:
        print("Player 4 is the Winner!")
    else:
        print("Multiple Players Draw")
        exit()
else:
    pass
