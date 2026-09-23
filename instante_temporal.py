import dic_er
import random

#Instante temporal
# Ejercicio 3
anglomesesList = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                  "november", "december"]

#EJERCICIO 1
def isBisiesto(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

#EJERCICIO 2
def isFechaCorrecta(d, m, y):
    #NO VÁLIDA BASE
    if d <= 0 or m <= 0 or d > 31 or m > 12:
        return False

    #ANÁLISIS DE CASOS
    #CASO MESES 31 días TRUE
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return True
    #CASO MESES 30 días menos FEBRERO
    elif m != 2 and d <= 30:
        return True
    #CASO FEBRERO y <= 28 true OR bisiesto and <= 29
    elif (m == 2 and d <= 28) or (m == 2 and isBisiesto(y) and d <= 29):
        return True
    #CASO NINGUNO: FALSE
    else:
        return False

def isHoraCorrecta(h, m, s):
    return 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60

#EJERCICIO 3
def fecha_es_menor_igual(f1, f2):
    if f1["year"] == f2["year"]:
        if f1["month"] == f2["month"]:
            if f1["day"] == f2["day"]:
                if f1["hour"] == f2["hour"]:
                    if f1["minutes"] == f2["minutes"]:
                        return f1["seconds"] <= f2["seconds"]
                    else:
                        return f1["minutes"] < f2["minutes"]
                else:
                    return f1["hour"] < f2["hour"]
            else:
                return f1["day"] < f2["day"]
        else:
            return f1["month"] < f2["month"]
    else:
        return f1["year"] < f2["year"]

#EJERCICIO 4
def generarFechaVálida(datos_ins_temp):
    #Genarar año
    y = random.randint(1, 9999)

    #Generar mes
    m = random.randint(1, 12)

    #Generar día en consecuencia:
    d = 0
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d = random.randint(1, 31)
    elif m == 2 and isBisiesto(y):
        d = random.randint(1, 29)
    elif m == 2:
        d = random.randint(1, 28)
    else:
        d = random.randint(1,30)
    datos_ins_temp["day"] = d
    datos_ins_temp["month"] = m
    datos_ins_temp["year"] = y

def anglomes_to_num(string):
    if string not in anglomesesList:
        return 0
    else:
        return anglomesesList.index(string) + 1

def validar_ins_temp(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_ins_temp].match(cadena)
    year = 0
    month = 0
    day = 0
    hour = 0
    minutes = 0
    seconds = 0
    dic = {}
    if m:
        f = 1
        while not m.group("year_f" + str(f)): f = f + 1
        # Caso campo presente en los 3 formatos
        year = int(m.group("year_f" + str(f)))
        month = -1
        day = int(m.group("day_f" + str(f)))
        hour = int(m.group("hour_f" + str(f)))
        minutes = int(m.group("minutes_f" + str(f)))
        seconds = 0

        # Caso formato 1
        if f == 1:
            month = int(m.group("month_f" + str(f)))

        # Caso formato 2
        if f == 2:
            month = anglomes_to_num(m.group("month_f" + str(f)).lower())
            momento = m.group("momento_f" + str(f))
            if hour == 12: hour = hour - 12
            if momento.lower() == 'pm' and hour != 12: hour = hour + 12

        # Caso formato 3
        if f == 3:
            month = int(m.group("month_f" + str(f)))
            seconds = int(m.group("seconds_f" + str(f)))

        dic["formato"] = f
        dic["year"] = year
        dic["month"] = month
        dic["day"] = day
        dic["hour"] = hour
        dic["minutes"] = minutes
        dic["seconds"] = seconds

        #Ver si día correcto
        if isFechaCorrecta(day, month, year): #la hora es correcta según la ER
            return dic
        else:
            return None
    else:
        return m