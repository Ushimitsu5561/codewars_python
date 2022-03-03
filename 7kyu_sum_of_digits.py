def sum_of_digits(digits):
    # summ = 0
    # ans = ''
    # if digits is None:
    #     return ""
    # elif isinstance(digits, str):
    #     for i in digits:
    #         summ += int(i)
    #         ans = " + ".join(digits)
    #     return f"{ans} = {summ}"
    # elif isinstance(digits, int):
    #     for i in str(digits):
    #         summ += int(i)
    #         ans = " + ".join(str(digits))
    #     return f"{ans} = {summ}"

    # if digits is None:
    #     return ""
    # else:
    #     for i in str(digits):
    #         summ += int(i)
    #         ans = " + ".join(str(digits))
    #     return f"{ans} = {summ}"
    # if digits is None:
    #     return ""
    # else:
    #     summ = sum([int(i) for i in str(digits) if isinstance(str(digits), str)])

    # if not digits is None:
    #     return f"{' + '.join(str(digits))} = {sum([int(i) for i in str(digits)])}"
    # else:
    #     return ""

    return "" if digits is None else f"{' + '.join(str(digits))} = {sum([int(i) for i in str(digits)])}"


def test_sum_of_digits():
    result = sum_of_digits("3433")
    assert result == "3 + 4 + 3 + 3 = 13", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits("64323")
    assert result == "6 + 4 + 3 + 2 + 3 = 18", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits("8")
    assert result == "8 = 8", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits(3433)
    assert result == "3 + 4 + 3 + 3 = 13", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits(64323)
    assert result == "6 + 4 + 3 + 2 + 3 = 18", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits(8)
    assert result == "8 = 8", f"Wrong answer {result} !"
    print(result)
    result = sum_of_digits(None)
    assert result == "", f"Wrong answer {result} !"
    print(result)


if __name__ == "__main__":
    test_sum_of_digits()
