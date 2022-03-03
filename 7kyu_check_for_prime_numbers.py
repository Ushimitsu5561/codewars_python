def is_prime(n):
    # if n == 0 or n == 1:
    #     return False
    # elif n > 1:
    #     for i in range(2, n):
    #         if (n % i) == 0:
    #             return False
    #     return True
    # else:
    #     return False

    return n > 1 and all(n % i for i in range(2, n))



def test_is_prime():
    result = is_prime(0)
    assert result == False, f"Wrong answer {result} !"
    print(result)

    result = is_prime(1)
    assert result == False, f"Wrong answer {result} !"
    print(result)

    result = is_prime(2)
    assert result == True, f"Wrong answer {result} !"
    print(result)

    result = is_prime(3)
    assert result == True, f"Wrong answer {result} !"
    print(result)

    result = is_prime(11)
    assert result == True, f"Wrong answer {result} !"
    print(result)

    result = is_prime(12)
    assert result == False, f"Wrong answer {result} !"
    print(result)

    result = is_prime(571)
    assert result == True, f"Wrong answer {result} !"
    print(result)

    result = is_prime(25)
    assert result == False, f"Wrong answer {result} !"
    print(result)


if __name__ == "__main__":
    test_is_prime()
