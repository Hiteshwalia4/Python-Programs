def strsort(s):
    lower = []
    upper = []
    odd_dgt = []
    even_dgt = []
    for char in s:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even_dgt.append(char)
            else:
                odd_dgt.append(char)
    return ''.join(sorted(lower) + sorted(upper) + sorted(odd_dgt) + sorted(even_dgt))


str = input("Enter any string- ")
print(strsort(str))
