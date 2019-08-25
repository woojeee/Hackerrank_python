if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


print([[i, j, k] for i in range(x + 1) for j in range(y + 1)
       for k in range(z + 1) if ((i + j + k) != n)])

# # for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
# if 문은 어떻게 처리? k에만 if문 걸어줘도 된다. k 하나만 변하면서 i + j + k != n 이 되게 할 수 있기 때문
