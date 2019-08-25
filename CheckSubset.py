# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t+1):
    num_a = int(input())
    a = set(map(int, input().split()))
    num_b = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
