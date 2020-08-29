
import math
# Program do obliczanie wartości liczby pi

# pi = 16 * math.atan(1 / 5) - 4 * math.atan(1 / 515)
pi = 22 / 7
# zaokraglenie = round(pi, 10000)
# print(" %.100f " % pi)
liczba_miejsc = 100
tekst = 'Cośtam'
dokladnosc = " %." + str(liczba_miejsc) + "f "
print(dokladnosc % pi)
print()
print(tekst.title())