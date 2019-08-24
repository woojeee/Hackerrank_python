# https://www.hackerrank.com/challenges/symmetric-difference/problem
# python set methods.

numOfFirst = int(input())
First_set = set(map(int, input().split()))
numOfSecond = int(input())
Second_set = set(map(int, input().split()))

dif_list = sorted(list(First_set.difference(Second_set).union(
    Second_set.difference(First_set))))

for a in dif_list:
    print(a)
