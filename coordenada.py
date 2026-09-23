import dic_er

#Coordenada
# Ejercicio 4
# 4.
# FORMATO1:Ej:30.0, -40.5;-25.05, +15.123
# (?P<lat_f1>(\+|-|)([0-9]|[1-8]\d|90)\.\d+)[ ]*,[ ]*(?P<lon_f1>(\+|-|)((([0-9]|[1-9]\d|1[0-7]\d)\.\d+)|180(?!\.)))
# FORMATO2:Ej:30° 0 ' 0.0000" N, 40° 30 ' 0.0000" W;25° 3 ' 0.0000" S, 15° 7 ' 22.8000" E
# (?P<lat_f2>(((?<!9))(([0-9]|[1-8]\d)°[ ]*([0-9]|[1-5]\d)'[ ]*([0-9]|[1-5]\d)\.\d{4}")|(90°[ ]*0'[ ]*0\.0000"))[ ]*(N|S))[ ]*,[ ]*(?P<lon_f2>((?<!1|18)(([0-9]|[1-9]\d|1[0-7]\d)°[ ]*([0-9]|[1-5]\d)'[ ]*([0-9]|[1-5]\d)\.\d{4}")|(180°[ ]*0'[ ]*0\.0000"))[ ]*(W|E))
# FORMATO3:Ej:0300000.0000N0403000.0000W;0250300.0000S0150722.8000E
# (?P<lat_f3>((0[0-8]\d{5}\.\d{4})|0900000\.0000)(N|S))(?P<lon_f3>((0\d{6}\.\d{4})|(1[0-7]\d{5}\.\d{4})|1800000\.0000)(W|E))
def validar_coord(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_coord].match(cadena)
    formato = 0
    grados_lat = 0
    minutos_lat = 0
    segundos_lat = 0
    letra_lat = '?'
    grados_lon = 0
    minutos_lon = 0
    segundos_lon = 0
    letra_lon = '?'
    dic = {}
    if m:
        f = 1
        while not m.group("lat_f" + str(f)): f = f + 1
        assert(f <= 3)
        # Caso formato 1
        if f == 1:
            # degrees = int(value)
            #   Obtener minutos (parte decimal)
            # minutes = (value - degrees) * 60
            #   Obtener segundos (parte decimal de los minutos)
            # seconds = (minutes - int(minutes)) * 60
            # minutes = int(minutes)
            # Guardar los decimales para los minutos y segudnos
            grados_lat_float = float(m.group("grad_lat_f" + str(f)))
            grados_lat = int(grados_lat_float)
            grados_lon_float = float(m.group("grad_lon_f" + str(f)))
            grados_lon = int(grados_lon_float)

            # Obtener las letras e invertir si < 0
            if grados_lat >= 0:
                letra_lat = 'N'
            else:
                grados_lat = -grados_lat
                grados_lat_float = -grados_lat_float
                letra_lat = 'S'
            if grados_lon >= 0:
                letra_lon = 'E'
            else:
                grados_lon = -grados_lon
                grados_lon_float = -grados_lon_float
                letra_lon = 'W'

            # Obtener los minutos con decimales (necesario para los segundos)
            minutos_lat = (grados_lat_float - grados_lat) * 60
            minutos_lon = (grados_lon_float - grados_lon) * 60

            # Obtener los segundos con decimales
            segundos_lat = (minutos_lat - int(minutos_lat)) * 60
            segundos_lon = (minutos_lon - int(minutos_lon)) * 60

            # Pasar los minutos a entero
            minutos_lat = int(minutos_lat)
            minutos_lon = int(minutos_lon)

        # Caso formato 2
        if f == 2:
            if m.group("grad_lat_f" + str(f)):
                grados_lat = int(m.group("grad_lat_f" + str(f)))
                minutos_lat = int(m.group("min_lat_f" + str(f)))
                segundos_lat = float(m.group("sec_lat_f" + str(f)))
            else:
                grados_lat = int(m.group("grad_lat_f" + str(f) + "_max"))
                minutos_lat = int(m.group("min_lat_f" + str(f) + "_max"))
                segundos_lat = float(m.group("sec_lat_f" + str(f) + "_max"))

            if m.group("grad_lon_f" + str(f)):
                grados_lon = int(m.group("grad_lon_f" + str(f)))
                minutos_lon = int(m.group("min_lon_f" + str(f)))
                segundos_lon = float(m.group("sec_lon_f" + str(f)))
            else:
                grados_lon = int(m.group("grad_lon_f" + str(f) + "_max"))
                minutos_lon = int(m.group("min_lon_f" + str(f) + "_max"))
                segundos_lon = float(m.group("sec_lon_f" + str(f) + "_max"))

            letra_lat = m.group("letra_lat_f" + str(f))
            letra_lon = m.group("letra_lon_f" + str(f))

        # Caso formato 3
        if f == 3:
            if m.group("grad_lat_f" + str(f)):
                grados_lat = int(m.group("grad_lat_f" + str(f)))
                minutos_lat = int(m.group("min_lat_f" + str(f)))
                segundos_lat = float(m.group("sec_lat_f" + str(f)))
            elif m.group("grad_lat_f" + str(f) + "_max"):
                grados_lat = int(m.group("grad_lat_f" + str(f) + "_max"))
                minutos_lat = int(m.group("min_lat_f" + str(f) + "_max"))
                segundos_lat = float(m.group("sec_lat_f" + str(f) + "_max"))

            if m.group("grad_lon_f" + str(f)):
                grados_lon = int(m.group("grad_lon_f" + str(f)))
                minutos_lon = int(m.group("min_lon_f" + str(f)))
                segundos_lon = float(m.group("sec_lon_f" + str(f)))
            elif m.group("grad_lon_f" + str(f) + "_max"):
                grados_lon = int(m.group("grad_lon_f" + str(f) + "_max"))
                minutos_lon = int(m.group("min_lon_f" + str(f) + "_max"))
                segundos_lon = float(m.group("sec_lon_f" + str(f) + "_max"))

            letra_lat = m.group("letra_lat_f" + str(f))
            letra_lon = m.group("letra_lon_f" + str(f))

        dic["formato"] = f

        dic["grados_lat"] = grados_lat
        dic["minutos_lat"] = minutos_lat
        dic["segundos_lat"] = segundos_lat
        dic["letra_lat"] = letra_lat

        dic["grados_lon"] = grados_lon
        dic["minutos_lon"] = minutos_lon
        dic["segundos_lon"] = segundos_lon
        dic["letra_lon"] = letra_lon
        return dic
    else:
        return m

def grados_a_decimal(coord):
    # Obtener los decimales
    lat_grados_float = coord["grados_lat"] + coord["minutos_lat"] / 60 + coord["segundos_lat"] / 3600
    lon_grados_float = coord["grados_lon"] + coord["minutos_lon"] / 60 + coord["segundos_lon"] / 3600
    if coord["letra_lat"] == 'S': lat_grados_float = -lat_grados_float
    if coord["letra_lon"] == 'W': lon_grados_float = -lon_grados_float
    coord_res = {}
    coord_res["lat"] = lat_grados_float
    coord_res["lon"] = lon_grados_float
    return coord_res