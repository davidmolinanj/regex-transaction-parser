import dic_er

#Teléfono
def sust_tlf_34(m):
    return "+34 " + m.group("numero_tlf")

# EJERCICIO 1
def validar_tlf(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_tlf].match(cadena)

    if m:
        dic = {}
        numero_encontrado = m.group("numero_tlf")
        numero_encontrado_w34 = dic_er.er_tlf.sub(sust_tlf_34, numero_encontrado)

        dic["numero_tlf"] = numero_encontrado
        dic["numero_tlf_wprefix"] = numero_encontrado_w34
        return dic
    else:
        return m
