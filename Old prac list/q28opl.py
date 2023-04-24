def copyfile():
    with open("Q27old.txt") as f:
        with open("q28old.txt","w") as g:
            b=f.read()
            g.write(b)

    print("File copied!!")
copyfile()

# Hello World
# Good morning
# Apple
# Mango Orange