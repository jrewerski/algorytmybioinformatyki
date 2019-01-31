
class ListProrityQueue:
    
    def __init__(self):
        """ Konstruktor"""
        self.liczby = []
    
    def isEmpty(self):
        """ Sprawdzanie czy pusta """
        return self.liczby == []
    
    def size(self):
        """ Zwraca rozmiar """
        assert hasattr(self, 'liczby')
        assert len(self.liczby) >= 0
        return len(self.liczby)
    
    def enqueue(self, liczba):
        """ Dodaje do kolejki liczbe """
        assert liczba == float or int
        self.liczby.insert(0, liczba)
        
    def dequeue(self):
        """ Obsluguje element o najwyzszej wartosci """
        assert self.size() > 0
        rozmiar = self.size()
        najwiekszy = 0
        for i in range(1,rozmiar):
            if self.liczby[i] > self.liczby[najwiekszy]:
                najwiekszy = i # szuka najwiekszego
        return self.liczby.pop(najwiekszy)
    
    def print(self):
        """ Drukuje kolejke"""
        if self.size() < 1:
            print("Brak kolejki")
        for i in range(self.size()):
            print(self.liczby[i], end =" ")
        print("\n")
            


if __name__ == '__main__':
    # Testy dla funkcji uruchomionej w main
    kopc = ListProrityQueue()
    for i in range(20):
        kopc.enqueue(i)
    assert kopc.size() == 20
    kopc.dequeue()
    assert kopc.size() == 19
    assert 19 not in kopc.liczby
    
