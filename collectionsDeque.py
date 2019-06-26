# list 클래스 상속!
class Deque(list):

    def dappend(self, num):
        self = self + [num]

    def dappendleft(self, num):
        self = [num] + self

    def dpop(self):
        popitem = self[-1]
        self = self[:-1]
        return popitem

    def dpopleft(self):
        popitem = self[0]
        self = self[1:]
        return popitem


d = Deque()

n = int(input())

for i in range(0, n):
    command = input()
    if " " in command:
        command, num = command.split(" ")
        print(command, num)
    if command == 'append':
        d.dappend(num)
        print(d)
    elif command == 'appendleft':
        d.dappendleft(num)
        print(d)
    elif command == 'pop':
        d.dpop()
        print(d)
    elif command == 'popleft':
        d.dpopleft()
        print(d)

for word in d:
    print(word, end=" ")
