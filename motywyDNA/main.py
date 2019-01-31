import Score as sc
import tree_projektI as tree

DNA1 = ['tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
        'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
        'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
        'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
        'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
        'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
        'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta',
        'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
        'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
        'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg']

T = 10
N = len("tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat")
L = 7

def BranchAndBoundMotifSearch(DNA, t, n, l):
    """ t - number of sample DNA sequences
    n - length of each DNA sequence
    l - length of the motif (l -mer)
    s=(s1, s2,… st) - array of motif’s starting
    positions"""
    assert l > 1
    assert n > 1
    assert DNA != [] 
    assert t > 1

    
    bestScore = 0
    i = 0 # poziom drzewa
    s_tree =[1]*t # pozycje startowe
    while True:
        assert i <= t
        if i < t: # poziom musi byc mniejszy od wysokosci
            s = [s_treex-1 for s_treex in s_tree]
            optimisticScore = sc.Score(s, DNA, l) + (t - i) * l
            # optymistyczny score dla nie do konca wypelnionych pozycji startowch np 1_ _ _ 
            # oszczedza zagladanie do (n–l + 1)^t-i lisci
            if optimisticScore < bestScore:
                s_tree, i = tree.Bypass(s_tree, i, t, n - l+1 )
                # pomijamy dzieci, poniewaz nie znajdziemy wsrod nich lepszego score od 
                # optymistycznego
            else:
                s_tree, i = tree.NextVertex(s_tree, i, t, n - l+1)
        else:
            s = [s_treex-1 for s_treex in s_tree]
            score = sc.Score(s, DNA, l)
            if score > bestScore: # jesli znalezlismy lepsze score 
                bestScore = score # ustawiamy je jako najlepsze
                bestMotif = [x for x in s] # i pozycje startowe dzieki ktorym mozna uzyskac score
            s_tree, i = tree.NextVertex(s_tree, i, t, n - l+1)
        if sum(s_tree) == 0: # jesli skonczymy na wierzcholku ( 0,0,...,0) przerywamy
            break
    return bestMotif

#print(BranchAndBoundMotifSearch(DNA1, T, N, L))


def BruteForceMotifSearch(DNA, t, n, l):
    assert l > 0
    assert n > 0
    assert DNA != [] 
    assert t > 0
    s_tree =[1]*t
    s = [0 for i in range(t)]
    # pozycje startowe
    bestScore = sc.Score(s, DNA, l+1) # score pierwszego liscia
    bestMotif = [x for x in s]
    while True:
        s_tree = tree.NextLeaf(s_tree, t, n - l+1) # nastepny lisc 
        s = [s_treex-1 for s_treex in s_tree]
        # przeszukiwanie po drzewie w celu znalezienia najlepszego score 
        if sc.Score(s, DNA, l) > bestScore:
            bestScore = sc.Score(s, DNA, l)
            bestMotif = [x for x in s]
        if sum(s_tree) == t:
            break
    return bestMotif

# print( BruteForceMotifSearch(DNA1, T, N, L))


if __name__ == "__main__":
    print("Testy funkcji: ")
    
    DNA2 = ['tactaaat',
            'aaaaaaaa',
            'ataaagta',
            'tcataaaa',
            'aaagacct']
    T = 5
    N = len('aggtactt')
    L = 3
    print(DNA2)
    print("BranchAndBound: ")
    motifs = BranchAndBoundMotifSearch(DNA2, T, N, L)
    print(motifs)
    for i in range(0,T):
           print(DNA2[i][motifs[i]:motifs[i]+L])
           
    motifs = BruteForceMotifSearch(DNA2, T, N, L)
    print("BruteForce: ")
    print(motifs)
    for i in range(0,T):
           print(DNA2[i][motifs[i]:motifs[i]+L])
    print("wszystkie motywy powinny być \"aaa\"")
    assert BranchAndBoundMotifSearch(DNA2, T, N, L) == [4, 0, 2, 4, 0]
    assert BruteForceMotifSearch(DNA2, T, N, L) == [4, 0, 2, 4, 0]
   
    
    
