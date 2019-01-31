import numpy as np

def Polar(promien, ile):
    """Funkcja zwraca wspolrzedne biegunowe i jednoczesnie ich kartezjanskie"""
    assert promien > 0, "Promien nie moze byc ujemny badz rowny 0"
    assert ile > 0, "Nie ma punktu dla ktorego mozna obliczyc wspolrzedne"
    theta = np.random.uniform(0.0, 2.0*np.pi, ile)
    # wybieramy katy pomiedzy 0 a 2pi(0 do ponad 6)(radiany)
    assert len(theta) > 0, "Blad napisania funkcji"
    r = promien*np.random.uniform(0.0, 1.0, ile)
    # wybieramy dla nich promien 
    assert len(r) > 0, "Blad napisania funkcji"
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # zamiana wspolrzednych biegunowych na kartezjanskie
    # x to jest cosinus kata theta a y to sinus tego kata
    assert len(x) & len(y) > 0
    return theta, r, x, y 

if __name__ == '__main__':
    # Testy dla funkcji uruchomionej w main
    assert Polar(1,1)[1] < 1
    assert Polar(2,1)[1] < 2
