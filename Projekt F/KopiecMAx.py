import math

class MaxHeap:
    
    def __init__(self):
        """ konstrukotor """
        self.keys = []
    def parent(self, i):
        """ Do ustalenia rodzica """
        return int((i-1)/2)
    
    def left(self, i):
        """ Indeks lewego syna """
        return (2*i+1)
    
    def right(self,i):
        """ Index prawego syna """
        return (2*i+2)
    
    def isEmpty(self): 
        """ Sprawdzenie, czy kopiec jest pusty """
        assert hasattr(self, 'keys')
        # zapewnia, ze obiekt ma klucze( dzialanie konstruktora)
        return self.keys == []
    
    def size(self):
        """ Zwraca rozmiar """
        assert hasattr(self, 'keys')
        assert len(self.keys) >= 0
        # zapewnia, ze obiekt klucze z ktorych bedzie liczona dlugosc kolejki
        return len(self.keys)
    
    def FixUp(self, i):
        assert i == int or float 
        """ Naprawia kopiec od dołu """
        while(self.keys[self.parent(i)] < self.keys[i] and i>=1):
            self.keys[self.parent(i)], self.keys[i] = self.keys[i], self.keys[self.parent(i)]
            i = self.parent(i)
            
    def FixDown(self, i):
        """ Naprawia kopiec od gory """
        assert i == int or float
        max1 = i
        if (self.left(i) <self.size() and self.keys[self.left(i)] > self.keys[max1]):
            max1 = self.left(i)
        if (self.right(i) <self.size() and self.keys[self.right(i)] > self.keys[max1]):
            max1 = self.right(i)
        if(max1!=i):
            self.keys[max1], self.keys[i] = self.keys[i], self.keys[max1]
            self.FixDown(max1) 
        
    def enqueue(self, liczba):
        """ Dodaje nowy element do koljeki """
        assert liczba == int or float
        self.keys.append(liczba)
        self.FixUp(self.size()-1) # konieczna jest naprawa kopca
    
    def dequeue(self):
        """ Obsluguje klucz o najwyzszym priorytecie, zwraca go i naprawia kopiec od dolu"""
        assert self.size() > 0
        max1 = self.keys[0]
        self.keys[self.size() -1], self.keys[0] =  self.keys[0], self.keys[self.size() -1]
        self.keys.pop(self.size()-1)
        self.FixDown(0)
        return max1
    
    def wydrukujKopiec(self):
        """ Drukuje kopiec wraz z podaniem pozimow """
        assert self.size() > 0 , "brak kopca do wydrukowania"
        assert self.isEmpty() == 0
        print("kopiec: ")
        i = 0
        while i < self.size():
            print("poziom: ", int(math.log2(i + 1)))  
            x = i      
           
            for x in range(i, self.size()):
               if x >= self.left(i):
                   break
               else:
                   print(self.keys[x], end = ' ')
            i = self.left(i)
            print("\n")
        
if __name__ == '__main__':
    print("Testy dla funkcji uruchomionej w main")
    kopc = MaxHeap()
    for i in range(20):
        kopc.enqueue(i)
    assert kopc.size() == 20
    kopc.wydrukujKopiec()
    kopc.dequeue()
    print("Dequeue")
    kopc.wydrukujKopiec()
    assert kopc.size() == 19
    assert kopc.keys[0] == 18
    
    
        
        
        
        
        
        
        
        