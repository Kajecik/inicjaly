import turtle


#1
#wspolrzedne
zolw = turtle.Turtle()
turtle.setworldcoordinates(0,0,700,700)
# litera P
#2
tablicaP0x = [118, 118,178,181,212,218]
tablicaP0y = [222,73,75,171,186,230]
tablicaP1x = [118,103,163,186,235,197]
tablicaP1y = [207,73,77,178,187,253]
tablicaP2x = [133,197,170,169,233,118]
tablicaP2y = [73,73,156,167,213,251]
tablicaP3x = [118,178,181,212,218,118]
tablicaP3y = [73,75,171,186,230,223]

# litera K
#3
tablica2P0x = [408,410,459,456,534,561,498,553,526,477,455,451]
tablica2P0y = [42,213,216,139,213,177,120,43,42,96,95,37]
tablica2P1x = [407,395,458,444,524,549,489,546,511,475,445,437]
tablica2P1y = [27,212,231,130,225,186,132,40,43,98,94,41]
tablica2P2x = [425,460,468,544,573,507,567,542,488,469,461,424]
tablica2P2y = [214,201,148,201,168,108,49,41,85,97,34,38]
tablica2P3x = [410,459,456,534,561,498,553,526,477,455,451,409]
tablica2P3y = [213,216,139,213,177,120,43,42,96,95,37,38]
 #4
for x in range(0,6):
    licznik = 0
    while True:
        szukana_wartosc_x =  (1-licznik)**3 * tablicaP0x[x] + 3 * (1 - licznik)**2\
                             * licznik * tablicaP1x[x] + 3*(1-licznik)* licznik**2 *\
                             tablicaP2x[x] + licznik**3 * tablicaP3x[x]
        szukana_wartosc_y = (1 - licznik) ** 3 * tablicaP0y[x] + 3 *\
                            (1 - licznik) ** 2 * licznik * tablicaP1y[x]\
                            + 3 * (1 - licznik) * licznik ** 2 * tablicaP2y[x]\
                            + licznik ** 3 * tablicaP3y[x]
        if(zolw.pos() == (0,0)):
            zolw.penup()
            zolw.goto(szukana_wartosc_x, szukana_wartosc_y)
            zolw.pendown()
        else:
            zolw.goto(szukana_wartosc_x, szukana_wartosc_y)
        licznik += 0.001
        if licznik > 1:
            break
#5
for x in range(0,12):
    licznik = 0
    while True:
        szukana_wartosc_x = (1 - licznik) ** 3 * tablica2P0x[x] + 3 * (1 - licznik) ** 2 \
                            * licznik * tablica2P1x[x] + 3 * (1 - licznik) * licznik ** 2 * \
                            tablica2P2x[x] + licznik ** 3 * tablica2P3x[x]
        szukana_wartosc_y = (1 - licznik) ** 3 * tablica2P0y[x] + 3 * \
                            (1 - licznik) ** 2 * licznik * tablica2P1y[x] \
                            + 3 * (1 - licznik) * licznik ** 2 * tablica2P2y[x] \
                            + licznik ** 3 * tablica2P3y[x]
        if (licznik == 0):
            zolw.penup()
            zolw.goto(szukana_wartosc_x, szukana_wartosc_y)
            zolw.pendown()
        else:
            zolw.goto(szukana_wartosc_x, szukana_wartosc_y)
        licznik += 0.001
        if licznik > 1:
            break
#6
turtle.exitonclick()