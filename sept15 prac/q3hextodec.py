def HexToDec(hex):
    l = len(hex)
    base = 1
    dec = 0

    for i in range(l - 1, -1, -1):
        if hex[i] >= '0' and hex[i] <= '9':
            dec += (ord(hex[i]) - 48) * base
            base = base * 16
        elif hex[i] >= 'A' and hex[i] <= 'F':
            dec += (ord(hex[i]) - 55) * base
            base = base * 16

    return dec

n = input("Enter a hexadecimal number- ")
print(HexToDec(n))
