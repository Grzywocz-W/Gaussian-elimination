def eliminacja_gaussa(macierz,wektor):
    n=len(macierz) #ilosc rownan
    rozszerzona=[macierz[i]+[wektor[i]] for i in range(n)]    #macierz rozszerzona
    for i in range(n-1):
        max_wiersz=i
        for k in range(i+1,n):   #ustawienie najwiekszego wiersza
            if abs(rozszerzona[k][i])>abs(rozszerzona[max_wiersz][i]):
                max_wiersz=k
        rozszerzona[i], rozszerzona[max_wiersz] = rozszerzona[max_wiersz],rozszerzona[i]

        for k in range(i,n-1):
            wspolczynnik=rozszerzona[k+1][i] / rozszerzona[i][i]
            for m in range(n+1):
                rozszerzona[k+1][m] -= (wspolczynnik*rozszerzona[i][m])
    #print(rozszerzona)
    wynik=[0]*n
    for i in range(n-1,-1,-1):
        suma=rozszerzona[i][n]
        for j in range(i+1,n):
            suma-=rozszerzona[i][j]*wynik[j]
        wynik[i]=suma/rozszerzona[i][i]
    return wynik

try:
    a=[]
    b=[]
    n=int(input("Podaj liczbę równań: "))
    for i in range(n):
        wiersz=list(map(float,input(f"Podaj wspolczynniki do wiersza {i+1} oddzielone spacjami:").split()))
        a.append(wiersz)
    for i in range(n):
        b.append(float(input(f"Podaj wartosc wyrazu wolnego dla rownania {i+1}: ")))
    wynik=eliminacja_gaussa(a,b)
    if wynik:
        print("Rozwiazanie ukladu rownan")
        for i,x in enumerate(wynik):
            print(f"x{i+1}={x:.4f}")
    else:
        print("Uklad nie jest oznaczony.")
except ValueError as e:
    print(f"Wystapil blad: {e}")
