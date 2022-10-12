#zad1
def imie(a , b):
    return(a+"."+b)
a="jan"
b="Kowalski"
print(imie(a,b))


#zad2
def foo(pierwsza,nazwisko):
    pom = pierwsza[0].title()
    return(pom+"."+nazwisko)
pierwsza = "jan"
nazwisko = "brzeczyszczykiewicz"
print(foo(pierwsza, nazwisko))
#zad3

def rok(a,b,c):
    d=str(a)+str(b)
    d=int(d)
    return(d-c)
a="22"
b="33"
c=44
print(rok(a,b,c))


#zad 4
def fun(imie,nazwisko,foo):
    return foo(imie,nazwisko)
print(fun("kamil","jarzyski",foo))


#zad 5
def funny(a,b):
    if a>0 and b>0 and b!=0:
        return(a/b)
print(funny(22,0))


#zad 6
suma=0
while(suma<100):
    a=int(input("podaj cyfre do zsumowania: "))
    suma+=a
    print(suma)


#zad 7
lista=[6,9,8,7]
def figaro(lista):
    return tuple(lista)
a=figaro(lista)
print(a)
print(type(a))
print(lista)
print(type(lista))


#zad8
list=[]
n=int(input("ile wartosci w tablicy: "))

i=0
while i<n:
    a=int(input(f"element na indeksie {i}: "))
    list.append(a)
    i=i+1

list=tuple(list)
print(list)


#zad 9
def dobry(a):
    dobry={1: "Fajniedziałek",
           2: "Ftorek",
           3: "srodaaaa;/",
           4: "czwartek",
           5: "piatek",
           6: "sobota",
           7: "nedzielnika"}
    return dobry[a]
print(dobry(3))


#zad 10
a="balwan"
def palindrom(napis):
    a=len(napis)-1
    for i in range(len(napis)):
        if napis[i] != napis[a-i]:
            return False
    return True
print(palindrom(a))






