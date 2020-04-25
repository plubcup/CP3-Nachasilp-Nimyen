def login():
    usernameInput = input("username :")
    passwordInput = input("password :")
    if usernameInput == "plubcup" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("------iShop------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userselected = int(input(">>"))
    return userselected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * 7 / 100)
    return result
def priceCalculate():
    price1 = int(input('First Product Price  :'))
    price2 = int(input('Second Product Price :'))
    return vatCalculate(price1 + price2)

if login() == True:
    showMenu()
    mn = menuSelect()
    if mn == 1:
        totalprice = float(input("Enter Price :"))
        print(vatCalculate(totalprice))
    elif mn == 2:
        print(priceCalculate())
else :
    print("---------------------")
    print("Error !!")