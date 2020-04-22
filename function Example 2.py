def login():
    userName = input("Username : ")
    passWord = input("Password : ")
    if userName == "plubcup" and passWord == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- Welcom ABC Shop -----")
    print("1.Vat Calculator")
    print("2 Price Calculator")

def menuSelected():
    userSelected = int(input(">>> : "))
    return userSelected

def vatCal(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result

def priceCal():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCal(price1+price2)

if login() == True :
    showMenu()
    menu = menuSelected()
    if menu == 1:
        totalprice = int(input("Enter Price : "))
        print(vatCal(totalprice))
    elif menu == 2:
        print(priceCal())
    else :
        print("Try Again !!")
else :
    print("Logni Not Success !!")
