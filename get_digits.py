digits = []


def get_digits(n):
    if n > 0:
        digits.insert(0, n % 10)
        get_digits(n // 10)


num = int(input("请输入个整数："))
get_digits(num)
print(digits)