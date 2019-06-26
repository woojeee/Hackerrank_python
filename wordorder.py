# Timeout!
# n = int(input())
# words = []
# wordset = []
# for i in range(0, n):
#     words.append(input())
# print(len(set(words)))
# for word in words:
#     if word not in wordset:
#         wordset.append(word)
#         print(words.count(word), end=" ")

n = int(input())
words = dict()

for i in range(0, n):
    word = input()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

print(len(words))
for value in words.values():
    print(value, end=" ")

# python 3.6부터 dict 순서 반영
