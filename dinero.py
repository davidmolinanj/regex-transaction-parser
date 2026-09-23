import dic_er

#Dinero
def validar_dinero(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_dinero].match(cadena)
    if m:
        dic = {}
        dinero = float(m.group("dinero_cantidad"))
        simbolo = m.group("dinero_simbolo")
        dic["dinero"] = dinero
        dic["simbolo"] = simbolo
        return dic
    else:
        return m

def dinero_to_string(datos):
    string_res = ""
    aux = datos["dinero"]
    str_aux = f"{aux:.2f}"
    string_res += str_aux
    string_res += datos["simbolo"]
    return string_res