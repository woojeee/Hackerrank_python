def merge_the_tools(string, k):
    # your code goes here
    # n/k 로 나눈 만큼 리스트.
    n = len(string)
    div_list = []
    for i in range(0, int(n/k)):
        # divide string into list
        temp_list = list(string[i*k:(i+1)*k])
        remove_overlap = []
        # print(temp_list)
        # remove overlap word
        for word in temp_list:
            if word not in remove_overlap:
                remove_overlap.append(word)
        # print(remove_overlap)
        # string으로 합쳐서 리스트에 저장
        div_list.append("".join(remove_overlap))

    for word in div_list:
        print(word)


string, k = input(), int(input())
merge_the_tools(string, k)
