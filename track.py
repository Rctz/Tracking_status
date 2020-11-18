from code.ems import ems

if __name__ == "__main__":
    re = ""
    barcode = input("Input your barcode: ")
    check = barcode.split(" ")
    if(check[0] == "ems"):
        re = ems(check[1])
    elif(check[0]== "kerry"):
        pass

    print(re.Response_message)
