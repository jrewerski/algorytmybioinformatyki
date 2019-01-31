
def Score(s, DNA, l):
    score = 0
    for i in range (l):
        # petla po pozycjach motywow w kolumnie
        cnt = dict(zip("actg",(0,0,0,0)))
        # Pusta Macierz profilu 
        for j, s_val in enumerate(s):
            # j - ilosc nici
            # s-val - przesuniecie w nici (nukleotyd)
            # s - krotka z pozycja startowa
            base = DNA[j][s_val+i]
            # zasada azotowa w j sek, w pozycji startowej s_val i w i-tej pozycji meru
            cnt[base] +=1
            # zlicza zasade i tworzy sie macierz profilu
        score += max(cnt.values())
        # dolicza do score maksymalna wartosc z kolumny macierzy 
    return score
