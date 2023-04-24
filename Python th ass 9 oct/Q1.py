x = input().split()
m = int(x[0])
n = int(x[1])

y= list()
happiness = 0

y = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in y:
    if i in A:
        k = happiness + 1
    if i in B:
        k = happiness - 1

print(happiness)
