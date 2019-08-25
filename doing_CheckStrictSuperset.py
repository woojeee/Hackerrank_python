# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
identifier = []
numofsets = int(input())
# print(a)
for i in range(numofsets + 1):
    compareset = set(map(int, input().split()))
    # print(compareset)
    if compareset.issubset(a) and compareset != a:
        identifier.append(1)
    else:
        identifier.append(0)

if 0 in identifier:
    print(False)
else:
    print(Tr)
