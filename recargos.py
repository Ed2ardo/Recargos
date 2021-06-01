



SMMLV = 908256
TRANSPORTE = 106454
V_HORA = SMMLV/240
HEDO = V_HORA * 1.25 # Hora extra diurna ordinaria
HENO = V_HORA * 1.75 # Hora extra nocturna ordinaria
HEDD = V_HORA * 2 # Hora extra diurna dominical
HEND = V_HORA * 2.5 # Hora extra nocturna dominical
RDF = V_HORA * 1.75 # recargo dominical o festivo
RNDF = V_HORA * 2.1 # Hora recargo nocturno, dominical o festivo
RNO = V_HORA * 1.35 #Recargo nocturna ordinaria
# MES = 30
festivos = {'mayo':(1,17), 
            'junio':(3,14), 
            'julio':(5,20),
            'agosto':(7,16),
            'septiembre':(),
            'octubre':(18),
            'noviembre':(1,15),
            'diciembre':(8,25)}

# print(festivos['mayo'])

# Hora ordinario: > 6:00 a <= 21:00
# Hora nocturna: > 21:00 <= 5:00 
# Formato 24 horas

HORAS = [] #ordinarias, recNoct.O, recDiurDom, recDomNoct

def festivo(dia, mes):
    if dia in festivos[mes]:
        return True
    else:
        return False

dia = 18
dia2 = False
mes = 'mayo'

diaFestivo = festivo(dia, mes)
dia2 = dia + 1
dia2 = festivo(dia2, mes)

def horas(h1,h2):
    if (h2-h1==8):
        if (h2<=16 and h1>=6): #Horas Ordinarias
            if (diaFestivo == False): # Evalua festivo
                ordinarias = h2 - h1
                HORAS.append(ordinarias)
                HORAS.append(ordinarias * V_HORA)
                recargoNocturnoO = 0
                HORAS.append(recargoNocturnoO)
                HORAS.append(recargoNocturnoO*RNO)
                # recDiurDom = 0
                # HORAS.append(recDiurDom)
                # HORAS.append(recDiurDom*RDF)
                # recDomNoct = 0
                # HORAS.append(recDomNoct)
                # HORAS.append(recDomNoct*RNDF)
            else:
                # ordinarias = 0
                # HORAS.append(ordinarias)
                # HORAS.append(ordinarias * V_HORA)
                # recargoNocturnoO = 0
                # HORAS.append(recargoNocturnoO)
                # HORAS.append(recargoNocturnoO*RNO)
                recDiurDom = h2 - h1
                HORAS.append(recDiurDom)
                HORAS.append(recDiurDom*RDF)
                recDomNoct = 0
                HORAS.append(recDomNoct)
                HORAS.append(recDomNoct*RNDF)
        elif (h2>=21 and h2<=24):  #Horas ordinarias y recargos
            if (diaFestivo == False):
                ordinarias = 21 - h1
                HORAS.append(ordinarias)
                HORAS.append(ordinarias * V_HORA)
                recargoNocturnoO = h2 - 21
                HORAS.append(recargoNocturnoO)
                HORAS.append((recargoNocturnoO*RNO))
                # recDiurDom = 0
                # HORAS.append(recDiurDom)
                # HORAS.append(recDiurDom*RDF)
                # recDomNoct = 0
                # HORAS.append(recDomNoct)
                # HORAS.append(recDomNoct*RNDF)
            else:
                # ordinarias = 0
                # HORAS.append(ordinarias)
                # HORAS.append(ordinarias * V_HORA)
                # recargoNocturnoO = 0
                # HORAS.append(recargoNocturnoO)
                # HORAS.append(recargoNocturnoO*RNO)
                recDiurDom = 21 - h1
                HORAS.append(recDiurDom)
                HORAS.append(recDiurDom*RDF)
                recDomNoct = h2 - 21
                HORAS.append(recDomNoct)
                HORAS.append(recDomNoct*RNDF)
        elif (h1>=0 and h1<6): #Recargos y Horas ordinarias
            if (diaFestivo == False):
                ordinarias = h2 - 6
                HORAS.append(ordinarias)
                HORAS.append(ordinarias * V_HORA)
                recargoNocturnoO = 6 - h1
                HORAS.append(recargoNocturnoO)
                HORAS.append((recargoNocturnoO*RNO))
                # recDiurDom = 0
                # HORAS.append(recDiurDom)
                # HORAS.append(recDiurDom*RDF)
                # recDomNoct = 0
                # HORAS.append(recDomNoct)
                # HORAS.append(recDomNoct*RNDF)
            else:
                # ordinarias = 0
                # HORAS.append(ordinarias)
                # HORAS.append(ordinarias * V_HORA)
                # recargoNocturnoO = 0
                # HORAS.append(recargoNocturnoO)
                # HORAS.append(recargoNocturnoO*RNO)
                recDiurDom = h2 - 6
                HORAS.append(recDiurDom)
                HORAS.append(recDiurDom*RDF)
                recDomNoct = 6 - h1
                HORAS.append(recDomNoct)
                HORAS.append(recDomNoct*RNDF)
    elif (h1>=17 and h1<24): #Ordinarias y Nocturnas 
        if dia2 == False:
            if (diaFestivo == False):
                if (h1<21):
                    ordinarias = 21 - h1
                    HORAS.append(ordinarias)
                    HORAS.append(ordinarias * V_HORA)
                    recargoNocturnoO = 3 + h2
                    HORAS.append(recargoNocturnoO)
                    HORAS.append((recargoNocturnoO*RNO))
                    # recDiurDom = 0
                    # HORAS.append(recDiurDom)
                    # HORAS.append(recDiurDom*RDF)
                    # recDomNoct = 0
                    # HORAS.append(recDomNoct)
                    # HORAS.append(recDomNoct*RNDF)
                else:
                    if h2 == 5 or h2 == 6:
                        ordinarias = 0
                        HORAS.append(ordinarias)
                        HORAS.append(ordinarias * V_HORA)
                        recargoNocturnoO = 8
                        HORAS.append(recargoNocturnoO)
                        HORAS.append((recargoNocturnoO*RNO))
                        recDiurDom = 0
                        HORAS.append(recDiurDom)
                        HORAS.append(recDiurDom*RDF)
                        recDomNoct = 0
                        HORAS.append(recDomNoct)
                        HORAS.append(recDomNoct*RNDF)
                    else:
                        ordinarias = 1
                        HORAS.append(ordinarias)
                        HORAS.append(ordinarias * V_HORA)
                        recargoNocturnoO = 7
                        HORAS.append(recargoNocturnoO)
                        HORAS.append((recargoNocturnoO*RNO))
                        recDiurDom = 0
                        HORAS.append(recDiurDom)
                        HORAS.append(recDiurDom*RDF)
                        recDomNoct = 0
                        HORAS.append(recDomNoct)
                        HORAS.append(recDomNoct*RNDF)
            else:
                if dia2 == False:
                    if (h1<21):
                        # ordinarias = 21 - h1
                        # HORAS.append(ordinarias)
                        # HORAS.append(ordinarias * V_HORA)
                        recargoNocturnoO = h2
                        HORAS.append(recargoNocturnoO)
                        HORAS.append((recargoNocturnoO*RNO))
                        recDiurDom = 21 - h1
                        HORAS.append(recDiurDom)
                        HORAS.append(recDiurDom*RDF)
                        recDomNoct = 3
                        HORAS.append(recDomNoct)
                        HORAS.append(recDomNoct*RNDF)
                    else:
                        if h2==5:
                            ordinarias = 0
                            HORAS.append(ordinarias)
                            HORAS.append(ordinarias * V_HORA)
                            recargoNocturnoO = 5
                            HORAS.append(recargoNocturnoO)
                            HORAS.append((recargoNocturnoO*RNO))
                            recDiurDom = 0
                            HORAS.append(recDiurDom)
                            HORAS.append(recDiurDom*RDF)
                            recDomNoct = 24 - h1
                            HORAS.append(recDomNoct)
                            HORAS.append(recDomNoct*RNDF)
                        elif (h2 == 6 or h2 == 7):
                            ordinarias = h2 - 6
                            HORAS.append(ordinarias)
                            HORAS.append(ordinarias * V_HORA)
                            recargoNocturnoO = 6
                            HORAS.append(recargoNocturnoO)
                            HORAS.append((recargoNocturnoO*RNO))
                            recDiurDom = 0
                            HORAS.append(recDiurDom)
                            HORAS.append(recDiurDom*RDF)
                            recDomNoct = 24 - h1
                            HORAS.append(recDomNoct)
                            HORAS.append(recDomNoct*RNDF)
                else: #Día 2 festivo
                    if (h1<21):
                        # ordinarias = 21 - h1
                        # HORAS.append(ordinarias)
                        # HORAS.append(ordinarias * V_HORA)
                        recargoNocturnoO = 0
                        HORAS.append(recargoNocturnoO)
                        HORAS.append((recargoNocturnoO*RNO))
                        recDiurDom = 21 - h1
                        HORAS.append(recDiurDom)
                        HORAS.append(recDiurDom*RDF)
                        recDomNoct = 3 + h2
                        HORAS.append(recDomNoct)
                        HORAS.append(recDomNoct*RNDF)
                    else:
                        if h2==5:
                            ordinarias = 0
                            HORAS.append(ordinarias)
                            HORAS.append(ordinarias * V_HORA)
                            recargoNocturnoO = 0
                            HORAS.append(recargoNocturnoO)
                            HORAS.append((recargoNocturnoO*RNO))
                            recDiurDom = 0
                            HORAS.append(recDiurDom)
                            HORAS.append(recDiurDom*RDF)
                            recDomNoct = 8
                            HORAS.append(recDomNoct)
                            HORAS.append(recDomNoct*RNDF)
                        elif (h2 == 6 or h2 == 7):
                            ordinarias = 0
                            HORAS.append(ordinarias)
                            HORAS.append(ordinarias * V_HORA)
                            recargoNocturnoO = 0
                            HORAS.append(recargoNocturnoO)
                            HORAS.append((recargoNocturnoO*RNO))
                            recDiurDom = h2 - 6
                            HORAS.append(recDiurDom)
                            HORAS.append(recDiurDom*RDF)
                            recDomNoct = 24 - h1 + 6
                            HORAS.append(recDomNoct)
                            HORAS.append(recDomNoct*RNDF)
        else:
            if (h1<21):
                ordinarias = 21 - h1
                HORAS.append(ordinarias)
                HORAS.append(ordinarias * V_HORA)
                recargoNocturnoO = 3
                HORAS.append(recargoNocturnoO)
                HORAS.append((recargoNocturnoO*RNO))
                recDiurDom = 0
                HORAS.append(recDiurDom)
                HORAS.append(recDiurDom*RDF)
                recDomNoct = h2
                HORAS.append(recDomNoct)
                HORAS.append(recDomNoct*RNDF)
            else:
                if h2==5:
                    ordinarias = 0
                    HORAS.append(ordinarias)
                    HORAS.append(ordinarias * V_HORA)
                    recargoNocturnoO = 3
                    HORAS.append(recargoNocturnoO)
                    HORAS.append((recargoNocturnoO*RNO))
                    recDiurDom = 0
                    HORAS.append(recDiurDom)
                    HORAS.append(recDiurDom*RDF)
                    recDomNoct = 5
                    HORAS.append(recDomNoct)
                    HORAS.append(recDomNoct*RNDF)
                elif (h2 == 6 or h2 == 7):
                    ordinarias = 0
                    HORAS.append(ordinarias)
                    HORAS.append(ordinarias * V_HORA)
                    recargoNocturnoO = 24 - h1
                    HORAS.append(recargoNocturnoO)
                    HORAS.append((recargoNocturnoO*RNO))
                    recDiurDom = h2 - 6
                    HORAS.append(recDiurDom)
                    HORAS.append(recDiurDom*RDF)
                    recDomNoct = 6
                    HORAS.append(recDomNoct)
                    HORAS.append(recDomNoct*RNDF)

# horas(22,6)
# print(HORAS)


