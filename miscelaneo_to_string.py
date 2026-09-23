import instante_temporal as i
import coordenada as c

#Miscelaneo instante & coordenada
def añadir_ceros_izquierda_hasta(s, n):
    n_ceros = n - len(s)
    ceros = n_ceros * '0'
    s = ceros + s
    return s

def inst_coord_to_string(datos):
    return inst_coord_to_string_in_format(datos, datos["formato"])

def inst_coord_to_string_in_format (datos, formato):
    assert isinstance(datos, dict)
    if not datos.get("formato", False):
        print("[ERROR] No has introducido un diccionario con atributo \"formato\"")
        return
    else:
        #formato = datos.get("formato")
        craw = {}   #campos_raw
        cstr = {}   #campos_string
        string_res = ""
        #CASO INSTANTE
        if datos.get("year", False):
            craw["year"] = datos.get("year")
            craw["month"] = datos.get("month")
            craw["day"] = datos.get("day")
            craw["hour"] = datos.get("hour")
            craw["minutes"] = datos.get("minutes")
            craw["seconds"] = datos.get("seconds")

            cstr["year"] = str(craw["year"])
            cstr["month"] = str(craw["month"])
            cstr["day"] = str(craw["day"])
            cstr["hour"] = str(craw["hour"])
            cstr["minutes"] = str(craw["minutes"])
            cstr["seconds"] = str(craw["seconds"])

            # f1:1945-08-06 08:15
            # f2:August 6, 1945 8:15 AM
            # f3:08: 15:00 06/08/1945
            if formato == 1:
                #print("instante, formato 1|", end="")
                cstr["year"] = añadir_ceros_izquierda_hasta(cstr["year"], 4)
                cstr["month"] = añadir_ceros_izquierda_hasta(cstr["month"], 2)
                cstr["day"] = añadir_ceros_izquierda_hasta(cstr["day"], 2)
                cstr["hour"] = añadir_ceros_izquierda_hasta(cstr["hour"], 2)
                cstr["minutes"] = añadir_ceros_izquierda_hasta(cstr["minutes"], 2)
                string_res = "-".join([cstr["year"], cstr["month"], cstr["day"]]) + " " + ":".join([cstr["hour"], cstr["minutes"]])
            elif formato == 2:
                #print("instante, formato 2|", end="")
                cstr["month"] = i.anglomesesList[craw["month"] - 1]
                momento = ''
                if craw["hour"] == 12:
                    cstr["hour"] = '12'
                    momento = 'PM'
                elif craw["hour"] == 0:
                    cstr["hour"] = '12'
                    momento = 'AM'
                elif 1 <= craw["hour"] <= 11:
                    #no hace falta tocar la cstr
                    momento = 'AM'
                else:
                    cstr["hour"] = str(craw["hour"] - 12)
                    momento = 'PM'
                cstr["minutes"] = añadir_ceros_izquierda_hasta(cstr["minutes"], 2)
                string_res = cstr["month"] + " " + cstr["day"] + ", " + cstr["year"] + " " + ":".join([cstr["hour"], cstr["minutes"]]) + " " + momento

            elif formato == 3:
                #print("instante, formato 3|", end="")
                cstr["hour"] = añadir_ceros_izquierda_hasta(cstr["hour"], 2)
                cstr["minutes"] = añadir_ceros_izquierda_hasta(cstr["minutes"], 2)
                cstr["seconds"] = añadir_ceros_izquierda_hasta(cstr["seconds"], 2)
                string_res = ":".join([cstr["hour"], cstr["minutes"], cstr["seconds"]]) + " "
                cstr["day"] = añadir_ceros_izquierda_hasta(cstr["day"], 2)
                cstr["month"] = añadir_ceros_izquierda_hasta(cstr["month"], 2)
                cstr["year"] = añadir_ceros_izquierda_hasta(cstr["year"], 4)
                string_res = string_res + "/".join([cstr["day"], cstr["month"], cstr["year"]])

            #Resultado
            #print(string_res)
            return string_res
        # f1:30.0, -40.5
        # f2:30° 0 ' 0.0000" N, 40° 30 ' 0.0000" W
        # f3:0300000.0000N0403000.0000W
        #CASO COORDENADA
        elif datos.get("letra_lat", False):
            craw["grados_lat"] = datos.get("grados_lat")
            craw["minutos_lat"] = datos.get("minutos_lat")
            craw["segundos_lat"] = datos.get("segundos_lat")
            craw["letra_lat"] = datos.get("letra_lat")
            craw["grados_lon"] = datos.get("grados_lon")
            craw["minutos_lon"] = datos.get("minutos_lon")
            craw["segundos_lon"] = datos.get("segundos_lon")
            craw["letra_lon"] = datos.get("letra_lon")

            cstr["grados_lat"] = str(craw["grados_lat"])
            cstr["minutos_lat"] = str(craw["minutos_lat"])
            cstr["segundos_lat"] = str(craw["segundos_lat"])
            cstr["letra_lat"] = str(craw["letra_lat"])
            cstr["grados_lon"] = str(craw["grados_lon"])
            cstr["minutos_lon"] = str(craw["minutos_lon"])
            cstr["segundos_lon"] = str(craw["segundos_lon"])
            cstr["letra_lon"] = str(craw["letra_lon"])
            if formato == 1:
                #print("coordenada, formato 1|", end="")
                # Obtener los decimales
                coord = c.grados_a_decimal(datos)
                string_res = str(coord["lat"]) + ", " + str(coord["lon"])
            elif formato == 2:
                #print("coordenada, formato 2|", end="")
                # f2:30° 0 ' 0.0000" N, 40° 30 ' 0.0000" W
                string_res = string_res + cstr["grados_lat"] + "° "
                string_res = string_res + cstr["minutos_lat"] + "' "
                sec_aux = craw["segundos_lat"]
                str_aux = f"{sec_aux:.4f}"
                string_res = string_res + str_aux + '''" '''
                string_res = string_res + cstr["letra_lat"] + ", "
                #longitud
                string_res = string_res + cstr["grados_lon"] + "° "
                string_res = string_res + cstr["minutos_lon"] + "' "
                sec_aux = craw["segundos_lon"]
                str_aux = f"{sec_aux:.4f}"
                string_res = string_res + str_aux + '''" '''
                string_res = string_res + cstr["letra_lon"]

            elif formato == 3:
                #print("coordenada, formato 3|", end="")
                #f3:0300000.0000N0403000.0000W
                string_res = string_res + añadir_ceros_izquierda_hasta(cstr["grados_lat"], 3)
                string_res = string_res + añadir_ceros_izquierda_hasta(cstr["minutos_lat"], 2)
                sec_aux = craw["segundos_lat"]
                str_aux = f"{sec_aux:.4f}"
                string_res = string_res + añadir_ceros_izquierda_hasta(str_aux, 7)
                string_res = string_res + cstr["letra_lat"]
                #longitud
                string_res = string_res + añadir_ceros_izquierda_hasta(cstr["grados_lon"], 3)
                string_res = string_res + añadir_ceros_izquierda_hasta(cstr["minutos_lon"], 2)
                sec_aux = craw["segundos_lon"]
                str_aux = f"{sec_aux:.4f}"
                string_res = string_res + añadir_ceros_izquierda_hasta(str_aux, 7)
                string_res = string_res + cstr["letra_lon"]
            # Resultado
            #print(string_res)
            return string_res
        else:
            print("[ERROR] No se pudo determinar la coordenada o instante de tiempo")