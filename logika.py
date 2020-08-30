# Logika w Pythonie - generator liczb pseudolosowych i analiza czasu ich dopasowywania

# Biblioteka umożliwiająca pracę z wieloma wątkami

import random

# Biblioteka do generowanie liczb pseudolosowych

import time
# Biblioteka operacji na czasie rzeczywistym
import statistics
# Biblioteka do uśredniania
histogram = []
powtorzenia = []

#kostka = [1, 2, 3, 4, 5, 6]     # 6 pól kostki
a = random.randint(1, 9)        # losowanie liczby 1-9 jako początku przedziału liczb do losowania w generatorze
b = random.randint(100,99999)   # j.w. tylko dla końca przedziału
test_logiczny = True            # wartość początkowa zmiennej zakańczającej działanie generatora
#c = 4                          # nie używane
generator = random.randint(a, b)
przebiegi_programu = []
d = 1
for i in range(10):             # ilość przebiegów procesu losowania
    przebiegi_programu.append(d)
    d += 1
iterator = [1]
pamiec_czasu = []

# ***

test_liczbowy = 0
for x in przebiegi_programu:
    czas = time.process_time()
    for x in iterator:

        if(generator == test_liczbowy):
            print('Logika = True')
            print(str(test_liczbowy))
            print(x)
            koniec_czasu = time.process_time() - czas
            print(str(koniec_czasu))
            pamiec_czasu.append(koniec_czasu)
            test_liczbowy = 0

            break

        else:

            print('Logika = False')
            test_liczbowy += 1
            iterator.append(generator)


print('*************************************************************')
print('*************************************************************')
print('*************************************************************')
print('$$$$$$$$$$$$$$$$$   Koniec symulacji   $$$$$$$$$$$$$$$$$$$$$$')
print('*************************************************************')
print('*************************************************************')
print('*************************************************************')
#print(pamiec_czasu)
liczba_pseudolosowa = statistics.mean(pamiec_czasu)
print('Liczba pseudolosowa: ' + str(liczba_pseudolosowa))
random.seed(liczba_pseudolosowa)
liczba_oczek = random.randint(1, 6)
print('Liczba oczek: ' + str(liczba_oczek))
histogram.append(liczba_oczek)
#print('Ilośc przebiegów tym razem to: ' + str(max(przebiegi_programu)))