def hex_output():
    decnum = 0
    hexnum = input("Enter a number to convert: ")
    for power, digit in enumerate(reversed(hexnum)):
        if(digit.lower() in ["a", "b", "c", "d", "e", "f"]):
            int_digit = hex_convert_letter(digit.lower())
        else:
            int_digit = digit
        decnum += int(int_digit) * (16 ** power)

    return decnum

def hex_convert_letter(letter):
    if(letter == "a"):
        return 10
    elif (letter == "b"):
        return 11
    elif (letter == "c"):
        return 12
    elif (letter == "d"):
        return 13
    elif (letter == "e"):
        return 14
    elif (letter == "f"):
        return 15

print(hex_output())