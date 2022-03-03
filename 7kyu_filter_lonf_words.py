def filter_long_words(sentence, n):
    # a =[]
    # y = sentence.split()
    # print(y)
    # for i in y:
    #     if len(i) > n:
    #         a.append(i)
    # return a
    return [x for x in sentence.split() if len(x) > n]


def test_filter_long_words():
    result = filter_long_words("The quick brown fox jumps over the lazy dog", 4)
    assert result == ['quick', 'brown', 'jumps'], f"Wrong answer {result} !"
    print(result)

if __name__ == "__main__":
    test_filter_long_words()