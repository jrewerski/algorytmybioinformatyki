import matplotlib.pyplot as plt
import polar
import cartesian as c
import DNA as d


# Modul cartesian

xx = c.Cartesian(30000, 2)
k = 2
ile = 30000
x_kolo = [[],[]]
x_poza = [[],[]]
for j in range(ile):
    if xx[0][j]**2 + xx[1][j]**2 <= 1:
        x_kolo[0].append(xx[0][j])
        x_kolo[1].append(xx[1][j])
    else:
        x_poza[0].append(xx[0][j])
        x_poza[1].append(xx[1][j])

print("Rozdział gęstosci dla wspolrzednych jest jednostajny, co potwierdza rysunek: ")

plt.plot(x_poza[0],x_poza[1], '.b')
plt.plot(x_kolo[0],x_kolo[1], '.g')
plt.show()

# Modul Polar

th, r, x, y = polar.Polar(10, 10000)
print("""Rodzdział gęstosci nie jest jednostajny dla losowych współrzędnych biegunowych, 
co można wyjasnić tym, że przy rosnącym promieniu potrzeba wiecej punktow aby zapelnic okrag
zakreslony przez promien""")
plt.plot(x, y, "m.", ms = 1) # ms - rozmiar markera
plt.show()

# Modul DNA

x = d.Motive(1000)
file0 = open("Motywy.txt", "w+")
file0.writelines("Motywy: ")
file0.writelines([str(x)])
file0.close()


