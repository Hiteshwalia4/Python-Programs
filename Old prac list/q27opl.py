def Count_vowel():
    with open("Q27old.txt") as f:
        b=f.read()
        print("Number of words in file are- ", len(b.split()))
        k=0
        for i in b:
            if i == "a" or i == "A" or i == "e" or i == "E" or i == "o" or i == "O" or i == "i" or i == "I" or i == "u" or i == "U":
                k=k+1


    print("Total numbers of vowels are- ",k)
Count_vowel()
#contents of file
# Hello World
# Good morning
# Apple
# Mango Orange