import numpy as np
    
def Motive(ile):
    """Funkcja tworzy n motywyow na podstawie macierzy p"""
    assert ile > 0, "Liczba motywow musi byc wiekszaod 0"
    p = np.array([
                [0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7], #A
                [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2 ], #C
                [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1 ], #G
                [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0 ]]) #T
    motywy = [] # lista wszystkich motywow
    for i in range(ile): # petla budujaca motywy
        zasada =""
        for k in range (8):
            x = np.random.uniform(0.0, 1.0, 1)
            assert x <= 1
            assert x >= 0
            # sprawdza w jakim zakresie znajduje sie wylosowany x
            # przypisuje mu odpowiednia zasade dla odpowieniej kolumny
            if x > (p[0][k] + p[1][k] + p[2][k]):
                zasada += 'T'
            elif x > (p[0][k] + p[1][k]):
                zasada += 'G'
            elif x > p[0][k]:
                zasada += 'C'
            else:
                zasada += 'A'
            assert len(zasada) > 0, "Blad tworzenia motywu"
        #zbudowane slowo dodajemy do listy motywow
        motywy.append(zasada)
    assert len(motywy) > 0, "Nie ma motywyow"
    return motywy

def TESTMotive(ile):
    """Funkcja testowa"""
    assert ile > 0, "Liczba motywow musi byc wiekszaod 0"
    p = np.array([
                [0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7], #A
                [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2 ], #C
                [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1 ], #G
                [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0 ]]) #T
    motywy = [] # lista wszystkich motywow
    for i in range(ile): # petla budujaca motywy
        zasada =""
        for k in range (8):
            x = 0.2
            if x > (p[0][k] + p[1][k] + p[2][k]):
                zasada += 'T'
            elif x > (p[0][k] + p[1][k]):
                zasada += 'G'
            elif x > p[0][k]:
                zasada += 'C'
            else:
                zasada += 'A'
            assert len(zasada) > 0, "Blad tworzenia motywu"
        #zbudowane slowo dodajemy do listy motywow
        motywy.append(zasada)
    assert len(motywy) > 0, "Nie ma motywyow"
    return motywy

assert TESTMotive(1) == ['ACACCAAA']
assert TESTMotive(2) == ['ACACCAAA','ACACCAAA']

if __name__ == '__main__':
    # Testy dla funkcji uruchomionej w main
    assert len(Motive(2)) == 2
    assert TESTMotive(1) == ['ACACCAAA']