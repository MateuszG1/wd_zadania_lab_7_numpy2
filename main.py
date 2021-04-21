import numpy as np

# #zad1
# a = np.array([1, 2, 3])
# b = np.array([5, 6, 7])
# print(a)
# print(b)
# print(a*b)
#
#
#
# #zad2
# c = np.arange(9).reshape(3, 3)
# d = np.arange(16).reshape(4, 4)
# print(c)
# print(c.min(axis=1))
# print(c.min(axis=0))
#
# print(d)
# print(d.min(axis=1))
# print(d.min(axis=0))
#
#
#
# #zad3
# print(a.dot(c))
# print(a.dot(d))



# #zad4
# calkowite = np.array([3, 4, 5])
# rzeczywiste = np.array([0.5, 2.5, 4.5])
# print(calkowite*rzeczywiste)



# #zad5
# macierz = np.arange(6).reshape(2,3)
# print(macierz)
# a = np.sin(macierz)
# print(a)
#
#
#
# #zad6
# macierz2 = np.arange(6).reshape(2,3)
# print(macierz2)
# b = np.cos(macierz2)
# print(b)
#
#
#
# #zad7
# print(a)
# print(b)
# print(a+b)



# #zad8
# macierz = np.arange(9).reshape(3, 3)
# for x in macierz:
#     print(x)



# #zad9
# macierz = np.arange(9).reshape(3, 3)
# for x in macierz.flat:
#     print(x)



# #zad10
# macierz = np.arange(81).reshape(9, 9)
# print(macierz)
# print(macierz.reshape(1, 81))
# print(macierz.reshape(3, 27))
# print(macierz.reshape(81, 1))
# print(macierz.reshape(27, 3))



#zad11
macierz = np.arange(12)
print(macierz)
a = macierz.reshape(3, 4)
print(a)
b = macierz.reshape(4, 3)
print(b)
c = macierz.reshape(2, 6)
print(c)

for x in a.flat:
    print(x)
print(" ")
for x in b.flat:
    print(x)
print(" ")
for x in c.flat:
    print(x)