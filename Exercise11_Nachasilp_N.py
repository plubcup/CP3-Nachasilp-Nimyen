num = int(input("Enter Number : "))
air = int(num-1)
text = int(2)

for x in range(1):
    print(" " * air , "*")
    for y in range(air):
        print(" " * (air-1) , "*" + "*" * text)
        air -= 1
        text += 2
