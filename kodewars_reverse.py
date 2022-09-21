
def reverse_words(s):
    """Реверс слов"""
    s = s[::-1]
    return s


def reverse_words_v2(str):
    """Второй вариант"""
    return " ".join(str.split(" ")[::-1])


def reverse_words_v3(st):
    """Третий вариант"""
    st = st.split(" ")
    st = st[::-1]
    st = " ".join(st)
    return st


# print(reverse_words("hello world!"))
# print(reverse_words_v2(str="hello world!"))
# print(reverse_words_v3(st="hello world!"))


class Reverse:

    def __init__(self):
        self.value_str = "hello world!"

    def revers_word(self):
        """Реверс слов"""
        self.value_str = self.value_str[::-1]
        return self.value_str

    def revers_word_2(self):
        """Второй вариант"""
        return " ".join(self.value_str.split(" ")[::-1])

    def revers_word_3(self):
        """Третий вариант"""
        self.value_str = self.value_str.split(" ")
        self.value_str = self.value_str[::-1]
        self.value_str = " ".join(self.value_str)
        return self.value_str


r = Reverse()

print(r.revers_word())
print(r.revers_word_2())
print(r.revers_word_3())
