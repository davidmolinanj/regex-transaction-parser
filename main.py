# SESIÓN 7
import sys
import comando as com
import dic_er

def tratar_argumentos(m):
    comando = sys.argv[1]
    print(comando)
    if comando == "-n":
        com.n(m)
    elif comando == "-sphone":
        com.sphone(m)
    elif comando == "-snif":
        com.snif(m)
    elif comando == "-stime":
        com.stime(m)
    elif comando == "-slocation":
        com.slocation(m)
    elif comando == "-generate":
        com.generate(m)

def tratar_opcion(s):
    cadena = s.strip()
    m = dic_er.diccionario_er[dic_er.patron_opcion].match(cadena)
    if m:
        tratar_argumentos(m)
    else:
        print("[ERROR] Sintaxis incorrecta de comando.")
        print("USO: -n <fichero> [<formato_tiempo> <formato_coordenada>] | -sphone <nºtlf> <fichero> | -snif <dni/nie> <fichero> | -stime <fecha_from> <fecha_to> <fichero> | -slocation <coordenada_origen> <distancia> <fichero> | -generate <fichero> <lineas>")
        return m

if __name__ == '__main__':
    opcion_str = " ".join(sys.argv[1:])
    tratar_opcion(opcion_str)
