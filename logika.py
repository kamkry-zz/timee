# Logika w Pythonie - generator liczb pseudolosowych i analiza czasu ich dopasowywania

import random

# Biblioteka do generowanie liczb pseudolosowych

import time
# Biblioteka operacji na czasie rzeczywistym
a = random.randint(1, 99)
b = random.randint(100,99999)
test_logiczny = True
c = 4
generator = random.randint(a, b)
przebiegi_programu = []
d = 1
for i in range(100):
    przebiegi_programu.append(d)
    d += 1
iterator = [1]
pamiec_czasu = []
test_liczbowy = 0

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
print(pamiec_czasu)
print('Ilośc przebiegów tym razem to: ' + str(max(przebiegi_programu)))