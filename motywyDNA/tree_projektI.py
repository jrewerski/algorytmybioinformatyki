def NextLeaf(a, L, k):
    # k = mer, a = pozycje startowe
    # l = liczba sekwencji DNA
    assert a != 0
    assert L >= 0
    assert k >= 0
    for i in reversed(range(L)):
        if a[i] < k:
            a[i] += 1
            break
        else:
            a[i] = 1
    return a


def NextVertex(a, i, L, k):
    # przesuwa do nastepnego wierzcholka
    # i  = poziom
    assert a != 0
    assert i >= 0
    assert L >= 0
    assert k >= 0
    if i < L:
        a[i] = 1
        return a, i+1
    # przesuwamy sie w glab drzewa
    else:
        for j in reversed(range(L)):
            if a[j] < k:
                a[j] += 1
                return (a, j+1)
            # odwiedzamy liscie
            a[j] = 0
    return a, 0


def Bypass(a, i, L, k):
    assert a != 0
    assert i >= 0
    assert L >= 0
    assert k >= 0
    # omijamy dzieci ojca na poziomie i
    for j in reversed(range(i)):
        if a[j] < k:
            a[j] += 1
            return a, j+1
        a[j] = 0
    return a, 0


if __name__ == "__main__":
    k = 2
    l = 3
    s = [4, 4, 3]
    print ("All leaves after", s)
    
    while True:
        s = NextLeaf(s, 3, k)
        print(s)
        if s == [1, 1, 1]:
            break
    
    print("\nWszystkie liscie i poziomy:")
    s = [0, 0, 0]
    level = 0
    while True:
        print (s, level)
        s, level = NextVertex(s, level, l, k)
        if level == 0:
            break
     
    print("\n Nie przechodzi przez ostatni lisc danego wierzcholka i pierwszy lisc koljenego w drzewie:")
    s = [0, 0, 0]
    level = 0
    while True:
        print (s, level) 
        if ((level == 2) and (s[0] != s[1])): 
            s, level = Bypass(s, level, l, k)
            print("przejscie na skroty")
        else:
            s, level = NextVertex(s, level, l, k)
        if level == 0:
            break

    print("\nNie przechodzi przez pierwszy lisc wierzcholka i ostatni kolejnego w drzewie:")
    s = [0, 0, 0]
    level = 0
    while True:
        print(s, level)
        if(level == 2) and (s[0] == s[1]):
            s, level = Bypass(s, level, 3, 2)
            print("przejscie na skroty")
        else:
            s, level = NextVertex(s, level, l, k)
        if level == 0:
            break
