id = input("ID :")
password = input("Password :")

if id == "plubcup" and password == "1234":
    print("----Welcome----")
    print("Select product")
    print("(1).Smart phone     5,000")
    print("(2).Powerbank       2,000")
    print("(3).Headphone         299")

    Sp = 5000
    Pb = 2000
    Hp = 299

    x = int(input("Select product :"))
    y = int(input("How much :"))

    if x == 1:
        print("------------------")
        print("Smart phone : ", Sp,"Bath")
        print("Total :", Sp * y, "Bath")
        print("------------------")
        print("---THANK YOU---")

    if x == 2:
        print("------------------")
        print("Powerbank : ", Pb, "Bath")
        print("Total :", Pb * y, "Bath")
        print("------------------")
        print("---THANK YOU---")

    if x == 3:
        print("------------------")
        print("Smart phone : ", Hp, "Bath")
        print("Total :", Hp * y, "Bath")
        print("------------------")
        print("---THANK YOU---")

else:
    print("Wrong!!!")

