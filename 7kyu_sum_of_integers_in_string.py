import re


def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r"[0-9]+", s))) # [0-9]+ -> "\d+"


def test_sum_of_integers_in_string():
    result = sum_of_integers_in_string("12.4")
    assert result == 16, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("h3ll0w0rld")
    assert result == 3, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("2 + 3 = ")
    assert result == 5, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter.")
    assert result == 1, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939.")
    assert result == 3868, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("Dogs are our best friends.")
    assert result == 0, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("C4t5 are 4m4z1ng.")
    assert result == 18, f"Wrong answer {result} !"
    print(result)
    result = sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog")
    assert result == 3635, f"Wrong answer {result} !"
    print(result)


if __name__ == "__main__":
    test_sum_of_integers_in_string()
