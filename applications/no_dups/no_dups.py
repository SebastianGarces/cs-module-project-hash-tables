def no_dups(s):
    # Your code here
    word_list = []
    s = s.split()
    [word_list.append(word) for word in s if word not in word_list]

    return " ".join(word_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
