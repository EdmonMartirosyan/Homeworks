def func(n):
    a = 1
    b = 10
    i = 2
    while i <= n:
        if i >= b:
            b *= 10
        a *= b
        a += i
        i += 1
    return a


print(func(18))
