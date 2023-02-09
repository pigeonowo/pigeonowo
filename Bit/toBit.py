import re


def toBitConvert(convertFrom, yourNumber):
    outcome = ""
    if convertFrom == "Bit":
        if re.search("^[0-1]*$", str(yourNumber)):
            outcome = yourNumber
        else:
            outcome = "This is not a Bit number"
    if convertFrom == "Decimal":
        bitnum = ''
        print("Converting to decimal....")
        while yourNumber >= 1:
            rest = str(yourNumber % 2)
            yourNumber = int(yourNumber / 2)
            bitnum+=rest
        outcome = bitnum[::-1]
    
    return outcome
        


