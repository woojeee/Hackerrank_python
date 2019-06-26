# def solve(s):
#     return " ".join(map(str.capitalize, s.split(" ")))
# map 메서드 쓸때는 str의 메서드라면 str.method int의 메서드라면 int.method

# 왜 아래 함수에서는 빈공간 split에서 다 없애고 다시 합칠때 빈공간 하나만???
# 여기서는 같게 나온다. but hackerrank 콘솔에서는 다르게 나옴.


def solve(s):
    a = s.split(" ")
    b = []
    for word in a:
        b.append(word.capitalize())
        print(b)
    return " ".join(b)


s = input()
result = solve(s)
print(result)
