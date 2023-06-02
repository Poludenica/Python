def max1(a, b):
    if a > b:
        return a
    return b


def LastFibo(n):
    if n  in [0,1] :
        return 1
    return LastFibo(n-1) + LastFibo(n-2)

def revers_range(num):
    print(num, end = ' ')
    if num > 0 :
        revers_range(num-1)
    