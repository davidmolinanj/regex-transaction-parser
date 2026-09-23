import dic_er

#DNI / NIE
# EJERCICIO 2
letrasDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
def determinar_letra_dni(dni):
    return letrasDNI[dni % len(letrasDNI)]

def nif_convertido_string(string):
    primer_caracter = string[0]

    # Caso NIE
    if primer_caracter in 'XYZ':
        numero_control = "2"
        if primer_caracter == 'X':
            numero_control = "0"
        elif primer_caracter == 'Y':
            numero_control = "1"

        return numero_control + string[1:]
    else:
        return string

def validar_dni_nie(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_dni_nie].match(cadena)

    if m:
        nif = m.group()
        num_nif = nif[:len(nif) - 1]
        letra_nif = nif[-1]
        #ver si es nie o dni ¿? por lo pronto no quiza no hace falta copium
        if determinar_letra_dni(int(nif_convertido_string(num_nif))) != letra_nif:
            #print("[ERROR] La letra del NIF no es correcta")
            return None
        else:
            return nif
    else:
        return m