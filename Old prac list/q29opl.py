def copy_alt_lines():
    with open("Q27old.txt") as f:
        with open("q29old.txt","w") as g:
            b=f.readlines()
            print(b)
            for i in range(len(b)):
                if i%2==0:
                    g.write(b[i])

copy_alt_lines()

# origial

# Hello World
# Good morning
# Apple
# Mango Orange

# after copying alternative lines
# Hello World
# Apple
