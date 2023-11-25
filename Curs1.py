# acesta este un comentariu pe o singura linie
'''
comentariu multi line
comentariu multi line
comentariu multi line
'''

print('salut lume')  # comentariu

# Variabile

prima_variabila = 'prima mea variabila'
print(prima_variabila)
x, y, z = 'orange', 'banana', 'chery'
print(x, y)

a = b = c = 'apple'
print(b)

nr_intreg = 10
numar_real = 3.14
boolean = True
boolean = False
null = None

print(30 * "!")

# Tipuri de date

nr_intreg = 10  # variabila tip integer
numar_real = 3.14  # variabila de tip float
boolean = True  # variabila de tip boolean
nume = 'George'  # variabila de tip string

lista_numere = [1, 2, 3, 4]
lista_cuvinte = ['mere', 'pere', 'banane']
tuplu = (10, 20, 30)
dictionar = {'cheie1': 'valoare1', 'cheie2': 'valoare2'}

suma = numar_real + nr_intreg
print('suma este: ', suma)

# contactenarea a 2 siruri

nume1 = 'Crina'
nume_complet = nume1 + ' Munteanu'
print('numele complet este ', nume_complet)

# test_variabila = nume1 + nr_intreg
# print(test_variabila)

print(30 * '!')

# functia Type

print('tipul de data al variabilei numar intreg', type(nr_intreg))  # CTRL + D copiaza randul
print('tipul de data al variabilei numar real', type(numar_real))
print('tipul de data al variabilei', type(nume))
print('tipul de data al variabilei', type(boolean))
print('tipul de data al variabilei', type(dictionar))

'''Functia Type Casting = 
proces prin care se transforma o valoare 
de un anumit tip intr-un alt tip de date'''

numar_intreg1 = 10
numar_real1 = float(numar_intreg1)
print(type(numar_intreg1))
print(type(numar_real1))

test_variabila = nume1 + ' ' + str(nr_intreg)
print(test_variabila)

# inglobarea variabilelor in cadrul instructiunii Print


nume = 'Dan'
an_nastere = '1990'
salariu = '5000,43'

print(nume + ' este nascut in anul ' + str(an_nastere) + ' si este angajat cu un salariu  ' + str(salariu) + ' lei')
# printare cu formatare
print(f'{nume} este nascuta in anul {an_nastere} si este angajata cu salariul {salariu} lei')


#functia input este o functie predefinita care permite interactiunea cu utilizatorul, prin citirea datelor de la tastatura

#nume = input('Introdu numele tau: ')
#print(f'Salut, {nume}')

# string methods = module pe care le vom importa

sir = 'Ana are mere'

print(sir)

sir2 = sir.replace('mere', 'pere')

print(sir2)

sir_litere_mari = sir.upper() #toate caracterele litere mari
print(sir_litere_mari)

sir_mic = sir.lower()
print(sir_mic)

sir_split = sir.split()
print(sir_split)

sir_index = sir.index("a")
print(sir_index)

sir_capitalizat = sir.capitalize()
print(sir_capitalizat)


lista = [1,2,3,4,5]

lista_nr = len(lista)

print(lista_nr)