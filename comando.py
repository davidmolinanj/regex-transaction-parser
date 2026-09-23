import sys
import random
import math
import compra

RADIO_TIERRA = 6367.45
OBJETOS_PRECIO = {
    "Samsung Galaxy Z Fold5 Negro Fantasma 1TB": 1899.99,
    "Apple iPhone 15 Pro Max Titanio Natural 512GB": 1499.00,
    "Google Pixel 8a Verde Menta 128GB": 499.90,
    "Xiaomi 14 Ultra Lente Leica 5G": 1299.00,
    "Motorola Edge 50 Pro 5G Púrpura": 699.99,
    "MacBook Air 15 M3 16GB RAM Gris Espacial": 1599.00,
    "Dell XPS 14 OLED i9 32GB RAM Plata Platino": 2599.00,
    "HP Spectre x360 16 Convertible 4K": 1750.00,
    "ASUS ROG Zephyrus G16 RTX 4080": 2999.00,
    "PC Sobremesa Custom i7-14700K 64GB RAM": 3500.00,
    "Microsoft Surface Pro 10 i5 16GB": 1099.00,
    "iPad Pro 11 M4 512GB Wi-Fi + Celular": 1399.00,
    "Kindle Paperwhite 16GB Agave Green": 159.99,
    "Samsung Galaxy Tab S9 Ultra 5G": 1199.00,
    "Sony PlayStation 5 Pro (Rumoreada)": 799.00,
    "Nintendo Switch OLED Edición Zelda": 349.99,
    "Auriculares Sony WH-1000XM6 Plata Estelar": 450.00,
    "Apple Watch Ultra 2 Correa Alpina Naranja": 899.00,
    "Controlador Xbox Elite Series 2 Core Blanco": 119.99,
    "Barra de Sonido Bose Smart Soundbar 900": 899.00,
    "Smart TV LG OLED G4 65 pulgadas": 2799.00,
    "Cámara Sony Alpha A7 IV Kit 28-70mm": 2499.00,
    "Impresora Multifunción Epson EcoTank ET-4850": 349.00,
    "Router Wi-Fi 7 TP-Link Archer GE800": 599.99,
    "Dron DJI Mini 4 Pro Fly More Combo": 1099.00,
    "Máquina de Café Nespresso Vertuo Next Cromo": 189.99,
    "Altavoz Inteligente Amazon Echo Studio": 199.99,
    "Disco Duro Externo SSD SanDisk Extreme 4TB": 299.99,
    "Monitor Curvo Samsung Odyssey G9 49 pulgadas": 1199.00,
    "Lápiz Óptico Apple Pencil Pro (USB-C)": 139.00,
    # ----------------------------------------------------
    # Objetos No Tecnológicos (~40)
    # ----------------------------------------------------
    "Sillón Reclinable Piel Genuina Color Coñac": 850.50,
    "Mesa de Comedor Redonda Madera Roble Nórdico": 620.00,
    "Alfombra Persa Shiraz 3x2 metros Lana Pura": 980.00,
    "Juego de Sábanas Algodón Egipcio 1000 Hilos Queen": 145.75,
    "Estantería Librero Modular de Bambú de 5 niveles": 110.50,
    "Lámpara de Pie Arco Acero Inoxidable y Mármol": 220.00,
    "Espejo de Pared Borde Dorado Circular 80cm": 95.90,
    "Set de 12 Tazas de Cerámica Artesanal Azul Marino": 45.99,
    "Pantalón Vaquero Levi's 501 Original W32 L34": 89.95,
    "Chaqueta de Cuero Genuina Estilo Biker Negra": 350.00,
    "Zapatillas Deportivas Adidas Samba Vegan Blanco/Negro Talla 42": 99.99,
    "Bufanda de Lana Cachemira Pura Color Burdeos": 125.00,
    "Camisa de Lino Manga Larga Azul Celeste": 55.00,
    "Gafas de Sol Ray-Ban Aviator Clásicas Polarizadas": 175.00,
    "Maleta de Viaje Rígida Samsonite Spinner Grande": 280.00,
    "Novela de Fantasía 'El Nombre del Viento' Edición Tapa Dura": 25.00,
    "Libro de Recetas 'Cocina Mediterránea Simple'": 18.50,
    "Revista 'National Geographic' Edición Mayo 2024": 7.95,
    "Set de Pinturas Acrílicas Profesional 24 Tubos": 42.00,
    "Juego de Cartas UNO Clásico": 8.99,
    "Puzzle de 1000 Piezas 'Paisaje Toscano'": 15.50,
    "Aceite de Oliva Virgen Extra 5 Litros Cosecha Temprana": 48.99,
    "Bolsa de Granos de Café Tostado 1kg Colombia Supremo": 22.50,
    "Queso Parmesano Reggiano DOP 500g": 19.95,
    "Botella de Vino Tinto Rioja Reserva 2018": 35.00,
    "Pan de Masa Madre Artesanal Grande": 4.50,
    "Caja de 12 Huevos Ecológicos Camperos": 6.99,
    "Taladro Percutor Bosch Professional 18V (Solo Cuerpo)": 159.00,
    "Set de 5 Destornilladores de Precisión Mango Ergonómico": 28.50,
    "Martillo de Carpintero Cabeza de Acero Forjado": 19.90,
    "Llave Inglesa Ajustable de Cromo Vanadio 12 pulgadas": 24.50,
    "Nivel de Burbuja Magnético de 60cm": 31.00,
    "Caja de Clavos para Madera 2kg Variados": 9.50,
    "Sierra Circular Manual 7.25 pulgadas": 75.00,
    "Bicicleta de Montaña Specialized Rockhopper Comp Talla M": 850.00,
    "Balón de Fútbol Adidas Euro 2024 Replica Talla 5": 38.99,
    "Esterilla de Yoga Antideslizante 6mm Corcho Natural": 49.00,
    "Raqueta de Tenis Head Speed Pro Graphene 360+": 185.00,
    "Mancuernas Ajustables de 20kg (Par)": 199.90,
    "Cuerda de Saltar de Velocidad con Rodamientos": 12.50
}

#Fichero
def file_not_found():
    print("[ERROR] No se encontró el archivo")
    print(
        "USO: -n <fichero> [<formato_tiempo> <formato_coordenada>] | -sphone <nºtlf> <fichero> | -snif <dni/nie> <fichero> | -stime <fecha_from> <fecha_to> <fichero> | -slocation <coordenada_origen> <distancia> <fichero> | -generate <fichero> <lineas>")

def normalizar(file, ft, fc):
    cont = 0
    cont_correctos = 0
    try:
        archivo = open(file)
    except FileNotFoundError:
        file_not_found()
    else:
        while True:
            linea = archivo.readline()
            if not linea:
                break  # Final del archivo
            else:
                datos = compra.validar_compra(linea)
                cont += 1
                if datos:
                    cont_correctos += 1
                    print(f"{cont_correctos}->", end="")
                    compra.escribir_compra(datos, ft, fc)
        print(f"[RESULTADO] \n{cont} compra(s) analizadas\n{cont_correctos} compra(s) con formato correcto\n{cont - cont_correctos} compra(s) con formato incorrecto")

def filtrar(file, condicion, filtro):
    cont = 0
    cont_filtro = 0
    cont_correctos = 0
    try:
        archivo = open(file)
    except FileNotFoundError:
        file_not_found()
    else:
        while True:
            linea = archivo.readline()
            if not linea:
                break  # Final del archivo
            else:
                datos = compra.validar_compra(linea)
                cont += 1
                if datos:
                    cont_correctos += 1
                    if condicion(datos, filtro):
                        cont_filtro += 1
                        print(f"{cont_filtro}->", end="")
                        print(linea, end="")
        print(
            f"[RESULTADO] \n{cont} compra(s) analizadas\n{cont_filtro} compra(s) que cumplen con la condicion\n{cont - cont_correctos} compra(s) con formato incorrecto")

def condicion_sphone(datos, filtro):
    return datos["tlf"]["numero_tlf"] == filtro

def condicion_snif(datos, filtro):
    return datos["dni-nie"] == filtro

def condicion_stime(datos, filtro):
    return compra.i.fecha_es_menor_igual(datos["ins_temp"], filtro["f2"]) and compra.i.fecha_es_menor_igual(filtro["f1"], datos["ins_temp"])

def distancia_haversine(coord1, coord2):
    decimal1 = compra.c.grados_a_decimal(coord1)
    decimal2 = compra.c.grados_a_decimal(coord2)

    phi1 = math.radians(decimal1["lat"])
    phi2 = math.radians(decimal2["lat"])

    delta_phi = math.radians(decimal2["lat"] - decimal1["lat"])
    delta_lambda = math.radians(decimal2["lon"] - decimal1["lon"])

    a = (math.sin(delta_phi / 2) ** 2) + \
        math.cos(phi1) * math.cos(phi2) * \
        (math.sin(delta_lambda / 2) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = RADIO_TIERRA * c
    return distancia

def condicion_slocation(datos, filtro):
    return distancia_haversine(datos["coordenada"], filtro["origen"]) <= filtro["distancia"]

#Programa
def n(m):
    ft = 3
    fc = 1
    if m.group("fc"):  # caso están los dos correctos
        ft = int(m.group("ft")) #o sysarg
        fc = int(m.group("fc")) #o sysarg
        normalizar(m.group("fichero_n"), ft, fc)
    else:
        try:
            sys.argv[3]  # ver si NO hay números
        except:
            normalizar(m.group("fichero_n"), ft, fc)
        else:
            print("[ERROR] [-n] Los formatos deben ser entre 1 y 3.")
            print("USO: -n <fichero> [<formato_tiempo> <formato_coordenada>]")

def sphone(m):
    filtrar(m.group("fichero_sphone"), condicion_sphone, m.group("numero_tlf"))

def snif(m):
    filtro = sys.argv[2]
    nif = compra.n.validar_dni_nie(filtro)
    if nif:
        filtrar(m.group("fichero_snif"), condicion_snif, nif)
    else:
         print("[ERROR] El NIF introducido para filtrar no es correcto.")
         print("USO: -snif <NIF válido> <fichero>")

def stime(m):
    filtro = {}
    filtro["f1"] = compra.i.validar_ins_temp(m.group("desde"))
    filtro["f2"] = compra.i.validar_ins_temp(m.group("hasta"))
    if filtro["f1"] and filtro["f2"]:
        if not compra.i.fecha_es_menor_igual(filtro["f1"], filtro["f2"]):
            print("[ERROR] La segunda fecha debe ser posterior.")
            print("USO: -stime <fecha_desde> <fecha_hasta> <fichero>")
        else:
            filtrar(m.group("fichero_stime"), condicion_stime, filtro)
    else:
        print("[ERROR] Alguna de las fechas introducidas no es correcta.")
        print("USO: -stime <fecha_desde> <fecha_hasta> <fichero>")

def slocation(m):
    filtro = {}
    filtro["origen"] = compra.c.validar_coord(m.group("coord_origen"))
    filtro["distancia"] = int(m.group("distancia"))
    filtrar(m.group("fichero_slocation"), condicion_slocation, filtro)

def generar_compra():
    dic = {}
    #tlf
    dic["tlf"] = {}

    #generar el número de tlf -> validar
    res_tlf = ""
    for i in range(9):
        entero_tlf = random.randint(0, 9)
        res_tlf += str(entero_tlf)
    dic["tlf"]["numero_tlf"] = res_tlf
    dic["tlf"]["numero_tlf_wprefix"] = "+34 " + res_tlf

    #dni-nie
    dic["dni-nie"] = {}

    #determinar primer caracter -> crear 7 más -> determinar_letra -> validar
    primer_caracter = '0123456789XYZ'
    primer_caracter = primer_caracter[random.randint(0, len(primer_caracter) - 1)]
    res_nif = ""
    for i in range(7):
        entero_nif = random.randint(0, 9)
        res_nif += str(entero_nif)
    numero_nif = primer_caracter + res_nif
    nif = numero_nif + compra.n.determinar_letra_dni(int(compra.n.nif_convertido_string(numero_nif)))
    dic["dni-nie"] = nif

    #ins_temp
    dic["ins_temp"] = {}

    #generar una valores correctos -> randomizar formato
    dic["ins_temp"]["hour"] = random.randint(0, 23)
    dic["ins_temp"]["minutes"] = random.randint(0, 59)
    dic["ins_temp"]["seconds"] = random.randint(0, 59)
    compra.i.generarFechaVálida(dic["ins_temp"])
    dic["ins_temp"]["formato"] = random.randint(1, 3)

    #coordenada
    dic["coordenada"] = {}

    #generar una coordenada -> randomizar formato
    dic["coordenada"]["grados_lat"] = random.randint(0, 89)
    dic["coordenada"]["minutos_lat"] = random.randint(0, 59)
    dic["coordenada"]["segundos_lat"] = random.uniform(0, 59.9999)
    letrasLat = 'NS'
    dic["coordenada"]["letra_lat"] = letrasLat[random.randint(0, len(letrasLat) - 1)]

    dic["coordenada"]["grados_lon"] = random.randint(0, 179)
    dic["coordenada"]["minutos_lon"] = random.randint(0, 59)
    dic["coordenada"]["segundos_lon"] = random.uniform(0, 59.9999)
    letrasLon = 'EW'
    dic["coordenada"]["letra_lon"] = letrasLon[random.randint(0, len(letrasLon) - 1)]

    dic["coordenada"]["formato"] = random.randint(1, 3)

    #texto_compra
    claves = list(OBJETOS_PRECIO.keys())
    clave = claves[random.randint(0, len(claves) - 1)]
    dic["textocompra"] = clave

    #dinero
    dic["dinero"] = {}

    #generar
    dic["dinero"]["dinero"] = OBJETOS_PRECIO.get(clave)
    simbolos = '$€'
    dic["dinero"]["simbolo"] = simbolos[random.randint(0, len(simbolos) - 1)]
    return dic

def escribir_compras_archivo(file, lineas):
    archivo = open(file, "w")
    for i in range(lineas):
        compra_generada = generar_compra()
        archivo.write(compra.compra_to_string(compra_generada, compra_generada["ins_temp"]["formato"], compra_generada["coordenada"]["formato"], False))
        archivo.write("\n")
    archivo.close()

def generate(m):
    file = m.group("fichero_generate")
    try:
        archivo = open(file)
    except FileNotFoundError:
        print(f"[INFO] Creando archivo {file} y escribiendo...")
        escribir_compras_archivo(file, int(m.group("lineas")))
    else:
        print("[INFO] El archivo ya existe, sobreescribiendo...")
        escribir_compras_archivo(file, int(m.group("lineas")))