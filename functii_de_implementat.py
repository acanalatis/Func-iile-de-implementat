# 1
def suma_cifrelor(n):
    s = 0
    for c in str(abs(n)):
        s += int(c)
    return f"Suma cifrelor lui {n} este {s}"


# 2
def cmmdc(a, b):
    if a == 0 and b == 0:
        return "Eroare: CMMDC nu este definit pentru (0, 0)"
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return f"CMMDC = {a}"


# 3
def cmmmc(a, b):
    if a == 0 or b == 0:
        return "Eroare: CMMMC nu este definit dacă unul dintre numere este 0"
    x, y = abs(a), abs(b)
    a0, b0 = x, y
    while y != 0:
        x, y = y, x % y
    return f"CMMMC = {abs(a0 * b0) // x}"


# 4
def numar_divizori(n):
    if n <= 0:
        return "Eroare: n trebuie să fie pozitiv"
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1 if i * i == n else 2
        i += 1
    return f"Numărul de divizori ai lui {n} este {cnt}"


# 5
def lista_prime_pana_la(n):
    if n < 2:
        return "Nu există numere prime"
    prime = []
    for x in range(2, n + 1):
        ok = True
        d = 2
        while d * d <= x:
            if x % d == 0:
                ok = False
                break
            d += 1
        if ok:
            prime.append(x)
    return f"Numere prime: {', '.join(map(str, prime))}"


# 6
def filtreaza_pare(lista):
    pare = []
    for x in lista:
        if x % 2 == 0:
            pare.append(x)
    if not pare:
        return "Nu există numere pare"
    return f"Numere pare: {', '.join(map(str, pare))}"


# 7
def produs_scalar(v1, v2):
    if len(v1) != len(v2):
        return "Eroare: vectorii au lungimi diferite"
    s = 0
    for i in range(len(v1)):
        s += v1[i] * v2[i]
    return f"Produsul scalar este {s}"


# 8
def medie_ponderata(valori, ponderi):
    if not valori or len(valori) != len(ponderi):
        return "Eroare: date invalide."
    suma_vp = 0
    suma_p = 0
    for i in range(len(valori)):
        suma_vp += valori[i] * ponderi[i]
        suma_p += ponderi[i]
    if suma_p <= 0:
        return "Eroare: suma ponderilor este zero"
    return f"Media ponderată este {suma_vp / suma_p}"


# 9
def rotire_dreapta(lista, k):
    if not lista:
        return "Lista este goala"
    k = k % len(lista)
    rotita = lista[-k:] + lista[:-k]
    return f"Lista rotită: {', '.join(map(str, rotita))}"


# 10
def interclaseaza(l1, l2):
    i = j = 0
    rez = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            rez.append(l1[i])
            i += 1
        else:
            rez.append(l2[j])
            j += 1
    while i < len(l1):
        rez.append(l1[i])
        i += 1
    while j < len(l2):
        rez.append(l2[j])
        j += 1
    return f"Interclasare: {', '.join(map(str, rez))}"


# 11
def elimina_duplicate(lista):
    rez = []
    for x in lista:
        if x not in rez:
            rez.append(x)
    return f"Fără duplicate: {', '.join(map(str, rez))}"


# 12
def frecventa_litere(text):
    frec = {}
    for c in text:
        if c != " ":
            frec[c] = frec.get(c, 0) + 1
    if not frec:
        return "Nu există caractere"
    return ", ".join(f"'{k}': {frec[k]}" for k in frec)



# 13
def cel_mai_frecvent_cuvant(text):
    cuvinte = text.split()
    if not cuvinte:
        return "Nu există cuvinte.="
    frec = {}
    for c in cuvinte:
        frec[c] = frec.get(c, 0) + 1
    max_cuv = cuvinte[0]
    for c in frec:
        if frec[c] > frec[max_cuv]:
            max_cuv = c
    return f"Cel mai frecvent cuvânt este '{max_cuv}'"


# 14
def este_isograma(text):
    t = text.replace(" ", "").lower()
    for c in t:
        if t.count(c) > 1:
            return f"'{text}' NU este isogramă"
    return f"'{text}' este isogramă"


# 15
def numere_distincte(lista):
    if not lista:
        return "Lista este goală"
    for x in lista:
        if lista.count(x) > 1:
            return "Lista conține elemente care se repetă"
    return "Toate numerele din listă sunt distincte"


# 16
def timp_in_format(secunde):
    if secunde < 0:
        return "Eroare: număr negativ"
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde = {h:02d}:{m:02d}:{s:02d}"


# 17
def parola_valida(parola):
    if len(parola) < 8:
        return "Parola invalidă: prea scurtă"
    are_litera = False
    are_cifra = False
    for c in parola:
        if c.isalpha():
            are_litera = True
        if c.isdigit():
            are_cifra = True
    if not are_litera:
        return "Parola invalidă: fără litere"
    if not are_cifra:
        return "Parola invalidă: fără cifre"
    return "Parola este validă"


# 18
def in_binar(n):
    if n < 0:
        return "Eroare: număr negativ"
    if n == 0:
        return "0"
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    return b


# 19
def numar_unic(lista):
    for x in lista:
        if lista.count(x) == 1:
            return f"Numărul unic este {x}"
    return "Eroare: condițiile nu sunt respectate"


# 20
def sunt_anagrame(a, b):
    a1 = a.replace(" ", "").lower()
    b1 = b.replace(" ", "").lower()
    if len(a1) != len(b1):
        return "Nu sunt anagrame"
    for c in a1:
        if a1.count(c) != b1.count(c):
            return "Nu sunt anagrame"
    return "Sunt anagrame"


# ================= PRINTURI =================

print(suma_cifrelor(123))
print(cmmdc(12, 18))
print(cmmmc(4, 6))
print(numar_divizori(6))
print(lista_prime_pana_la(10))
print(filtreaza_pare([1, 2, 3, 8, 10]))
print(produs_scalar([1, 2, 3], [4, 5, 6]))
print(medie_ponderata([8, 9, 10], [1, 2, 1]))
print(rotire_dreapta([1, 2, 3, 4, 5], 2))
print(interclaseaza([1, 2, 5], [2, 7]))
print(elimina_duplicate([1, 4, 2, 4, 1, 7]))
print(frecventa_litere("ana are mere"))
print(cel_mai_frecvent_cuvant("ana are mere ana"))
print(este_isograma("Ana are mere"))
print(numere_distincte([1, 2, 3]))
print(timp_in_format(3661))
print(parola_valida("abc12345"))
print(in_binar(5))
print(numar_unic([2, 3, 2, 4, 4]))
print(sunt_anagrame("listen", "silent"))
