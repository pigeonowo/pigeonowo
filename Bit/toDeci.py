import re

def toDeciConvert(convertFrom, yourNumber):
    print("test")
    outcome = ""
    print(yourNumber)
    if convertFrom == "Bit":
        if re.search("^[0-1]*$", str(yourNumber)):
            strnumber = str(yourNumber)
            outcome = int(strnumber, 2)
        else:
            outcome = "This is not a Bit number"
    if convertFrom == "Decimal":
        outcome = yourNumber
    
    return outcome