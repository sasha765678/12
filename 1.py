def fun(n):
    if n < 100:
        fun(n + 1)
        print(n)


fun(1)

