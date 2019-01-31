class Node:
    def __init__(self, initdata):
        """ Konstrukotr """
        self.data = initdata
        self.next = None
        
    def getData(self):
        """ Zwraca wartosc wezla """
        return self.data
    
    def getNext(self):
        """ przekierowanie wezla """
        return self.next
    
    def setData(self, newdata):
        """ Ustala wartosc wezla """
        self.data = newdata
    
    def setNext(self, newnext):
        """ ustala przekierowanie do kolejnego wezla"""
        self.next = newnext

class NodeList:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        """ Dodaje wezel """
        assert item == int or float
        newNode = Node(item) # stworzenie wezla
        newNode.setNext(self.head) 
        self.head = newNode
    
    def size(self):
        """ zwraca ilosc wezlow"""
        current = self.head
        count = 0
        while current!=None: # dopoki istnieja wezly
            count = count + 1
            current = current.getNext()
        return count
    
    def isEmpty(self):
        """Sprawdza czy lista jest pusta """
        return self.head == None
    
    def search(self, item):
        """ Szuka wezla """
        assert item == float or int
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item: # jesli sie znalazl
                found = True
            else:
                current  = current.getNext()
        return found
    
    def Remove(self, item):
        """ usuwa wezel i laczy odpowiednio kolejny i poprzedzajacy wezel"""
        assert item == float or int
        current = self.head
        previous = None
        while current:
            if current.getData() == item: # wyszukanie
                if previous:
                    previous.setNext(current.getNext()) #laczenie
                else :
                    self.head = current.getNext() 
                return current.getData() # zwraca wartosc usunieta
            previous = current
            current = current.getNext()
        return False 
          
    def getMax(self):
        """ Obsluguje wezel o max wartosci """
        current = self.head
        maxkey = 0
        while current != None: # wyszukanie najwiekszego 
            if current.getData() > maxkey:
                maxkey = current.getData()
            current = current.getNext() 
        self.Remove(maxkey) # usuniecie i zwrocenie
        return maxkey
    
if __name__ == '__main__':
    """testy dla klasy Nodelist uruchomionej w main"""
    kopc = NodeList()
    assert kopc.isEmpty() == True
    for i in range(20):
        kopc.add(i)
    assert kopc.search(9) == True
    assert kopc.size() == 20
    kopc.getMax()
    assert kopc.size() == 19
    for i in range(19):
        kopc.getMax()
    assert kopc.isEmpty() == True
    
    
    
    
    
    
    
    
    
                
    