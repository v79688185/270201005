choose = input("Choose what you want. \n 1: Binary to hexadecimal. \n 2:Hexadecimal to binary.\n Choose 1 or 2:")
if choose == "1":
    binary = input("Enter the binary: ")
    binarylist = []
    sumbinary=0
    for i in binary:
        binarylist.append(i)
    binarylist.reverse()   
    for i in binarylist:
        if i == "0":
           sumbinary += int(i)
        elif i == "1" :
           sumbinary = sumbinary + (2 ** binarylist.index(i)) 
           binarylist[binarylist.index(i)] = "0"
    print(f"hexadecimal represenation is{sumbinary}.")       
if choose == "2": 
    lastBinary = ""
    newstring = ""
    binarylist1=[]
    hexadecimalText = input("\nHexadecimal value: ")
    while int(hexadecimalText) > 0:
       addBinary = int(hexadecimalText) % 2
       lastBinary += str(addBinary)
       hexadecimalText = (int(hexadecimalText) / 2) // 1
    for i in lastBinary:
        binarylist1.append(i)
    binarylist1.reverse()
    for i in binarylist1 :
        newstring = newstring + i
    print(f"Binary representation is {newstring}") 