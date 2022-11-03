def fib(n:int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(7))

def power(number: int, n: int) -> int:
    if number == 0:
        return 1
    if n == 0:
        return 1
    else:
       return number*power(number,n-1)

print(power(3,4))


def reverse(txt: str) -> str:
    return txt[::-1]
print(reverse("Grzeorz Brzeczyszczykiewicz"))

def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return n*factorial(n-1)
print(factorial(3))


def prime(n: int, i=2):
    if n == i:
        return True

    if n % i == 0:
        return False

    return prime(n, i=i + 1)


def remove_duplicates(txt: str) -> str:
    if len(txt) == 1:
        return txt

    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])

    return txt[0] + remove_duplicates(txt[1:])


def n_sums(n: int, i: int = 0, sum1: int = 0, sum2: int = 0, l1=[]) -> list[int]:
    if i == 0:
        i = 10 ** (n - 1)

    if i == 10 ** n - 1:
        return l1

    if i < 10 ** n:
        i = str(i)
        for j in range(len(i)):
            if j % 2 == 0:
                sum1 += int(i[j])
            else:
                sum2 += int(i[j])

        if sum1 == sum2:
            l1.append(int(i))

        return n_sums(n, int(i) + 1, )

    
