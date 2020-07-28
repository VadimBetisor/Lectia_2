# 1.Ce valoare o sa contina variabila a după execuția codului ?
a = 10
a += len(str(a))
a = str(a)
print(a)
        # Raspuns: 12
# 2. Codul de mai jos conține o eroare, modificați codul astfel încît programul să funcționze corect.
print("In padurea cu alune aveau casa " + "2" + " pitici")
# 3. Ce valoare o sa contina variabila a dupa executia codului ?
a = 10
a + 1
print(a)
        # Raspuns: 10
# 4. Codul de mai jos contine o erroare, Modificati codul ca nu apara erroare?
a=10
a += 1
print(a)
        # Raspuns:11
# 5. Scrieti un program care primeste la input numele fisierului (text.txt, program.java) si intoarce extesia lui (txt, java).
# Scriere în fişier
f = open('test.txt', 'w')
f.write('text de test')
f.close()

# Citire din fişier
f = open('test.txt', 'r')
print(f.read())
f.close()


# 6. Fie următoarea listă: a = ['a', 'b', 'c', 'd']
a = ['a', 'b', 'c', 'd']
print(a)
# 6.1                Ce valoare are expresia a[int(int('3' * 2) // 11)] ?
a=(int(int('3' * 2)) // 11)
print(a)
        # Raspuns: 3
# 6.2                Adaugati o valoare nouă în lista a pe prima poziție.
a = ['a', 'b', 'c', 'd']
a.insert(0,'x')
print(a)
# 6.3                Ștergeți ultimele 2 valori din lista.
del a[-1]
del a[-2]
print(a)
# 6.4                Ordonati lista a descrescator
a = ['a', 'b', 'c', 'd']
print(a)
a.sort(reverse=True)
print(a)
# 6.5                Creați o listă nouă b care sa conțină toate elementele din lista a cu excepția primelor 2 elemente.
a = ['a', 'b', 'c', 'd']
print(a)
b=a
del b[0:2]
print(b)
