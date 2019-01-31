import numpy as np

def Cartesian(ile, k):
    """Funkcja losuje i zwraca wspolrzedne kartezjanskie
       punktu w k wymiarowej przestrzeni"""
    assert k > 0, "Wymiar musi być wiekszy od 0"
    assert ile > 0, "Ilosc punktow musi byc wieksza od 0"
    x = [] # lista list, w ktorej ostatnia reprezentuje wspolrzedne punktu w 
    # wymiarze k
    for i in range (1,k+1):
        for j in range(1,ile+1):
            y = 2*np.random.rand(j)-1 # losuje liczby i dodaje do listy y
        x.append(y) # dodaje liste y do listy x
    assert len(x) > 0, "Blad napisania funkcji"
    return x

if __name__ == '__main__':
    # Testy dla funkcji uruchomionej w main
    assert Cartesian(1,1)[0][0] <= 1
    assert Cartesian(2,2)[1][1] <= 1
