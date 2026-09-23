import dic_er
import telefono as t
import nif as n
import instante_temporal as i
import coordenada as c
import dinero as d
import miscelaneo_to_string as m

#Compra
def validar_compra(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_compra].match(cadena)

    lista = cadena.split(";")
    nif = n.validar_dni_nie(lista[1])
    fecha = i.validar_ins_temp(lista[2])
    if m and nif and fecha: #Comprobar si la fecha y el nif es válido, no lo comprueba la ER
        dic = {}
        dic["tlf"] = t.validar_tlf(lista[0])
        dic["dni-nie"] = nif #validar_dni_nie(lista[1])
        dic["ins_temp"] = fecha
        dic["coordenada"] = c.validar_coord(lista[3])
        dic["textocompra"] = lista[4].strip()
        dic["dinero"] = d.validar_dinero(lista[5])
        if dic["tlf"] and dic["dni-nie"] and dic["ins_temp"] and dic["coordenada"] and dic["textocompra"] and dic["dinero"]:
            return dic
        else:
            return None
    else:
        return None

def compra_to_string(datos, ft, fc, prefix_tlf = True):
    string_res = ""
    if prefix_tlf:
        string_res += datos["tlf"]["numero_tlf_wprefix"] + " ; "
    else:
        string_res += datos["tlf"]["numero_tlf"] + " ; "
    string_res += datos["dni-nie"] + " ; "
    string_res += m.inst_coord_to_string_in_format(datos["ins_temp"], ft) + " ; "
    string_res += m.inst_coord_to_string_in_format(datos["coordenada"], fc) + " ; "
    string_res += datos["textocompra"] + " ; "
    string_res += d.dinero_to_string(datos["dinero"])
    return string_res

def escribir_compra(datos, ft, fc):
    if datos:
        print(compra_to_string(datos, ft, fc))
        return compra_to_string(datos, ft, fc)