menuList = []
priceList = []
def showBill():
    totalprice = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalprice = 0
        totalprice += int(priceList[number])
        print("Total is :" , totalprice, "THB")
while True:
    menuName = input("Please enter menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price:")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()


