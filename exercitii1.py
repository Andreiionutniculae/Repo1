#1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
#O zona din memorie careia i se atribuie o valoare


# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# -string
# -int
# -float
# -bool
# Observație: Valorile vor fi alese de tine după preferințe.


string = 'carte'
int = 2023
float = 10.06
bool = False

#3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(string))
print(type(int))
print(type(float))
print(type(bool))

#4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
#Verifică tipul acesteia.

x = round(float)
print(x)
print(type(x))


#5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
#Rezolvă nepotrivirile de tip prin ce modalitate dorești.

print(f'{string.capitalize()}a a aprut in anul {int} la pretul de {float} lei.')

#6. Citește de la tastatură:
#   numele;
#   prenumele.
# Afișează: 'Numele complet are x caractere'.


nume = 'Niculae'
prenume = 'Andrei'

print(len(nume + ' ' + prenume) - 1)


x = sum(int(len(nume)) + int(len(prenume)))
print(x)