nm_set = set(map(int, input().split(" ")))
referset = set(map(int, input().split(" ")))
happyset = set(map(int, input().split(" ")))
unhappyset = set(map(int, input().split(" ")))

count = 0

for a in referset:
    if a in happyset:
        count += 1
    if a in unhappyset:
        count -= 1

print(count)
