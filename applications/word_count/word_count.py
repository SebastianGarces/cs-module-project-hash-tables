def word_count(s):
    # Your code here

    d = dict()

    char_list = '"":;.,-+=/\|[]{}()*^&'

    new_s = s.lower().replace("\t", " ").replace(
        "\n", " ").replace("\r", " ").split(" ")

    for word in new_s:
        new_word = word.strip(char_list)

        if new_word not in d and new_word != "":
            d[new_word] = 1
        elif new_word != "":
            d[new_word] += 1

    print(d)
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
