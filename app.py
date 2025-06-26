import sqlite3

def generar_trigramas(texto, eliminar_duplicados=False):
    if not texto:
        return ""

    texto = texto.upper()
    trigramas = set() if eliminar_duplicados else []

    palabras = [p for p in texto.split() if len(p) >= 3]

    if not palabras:
        texto_sin_espacios = texto.replace(" ", "").strip()
        for i in range(len(texto_sin_espacios) - 2):
            trig = texto_sin_espacios[i:i+3]
            if eliminar_duplicados:
                trigramas.add(trig)
            else:
                trigramas.append(trig)
    else:
        for palabra in palabras:
            for i in range(len(palabra) - 2):
                trig = palabra[i:i+3]
                if eliminar_duplicados:
                    trigramas.add(trig)
                else:
                    trigramas.append(trig)

    return " ".join(sorted(trigramas)) if eliminar_duplicados else " ".join(trigramas)

# --- Parte 1: Pedir al usuario una palabra e imprimir el trigram ---
entrada = input("Ingrese un texto: ")
resultado = generar_trigramas(entrada, eliminar_duplicados=True)
print("Trigramas generados:", resultado)

# --- Parte 2: Ejemplo de uso con base de datos SQLite (comentado) ---

"""
# Supongamos que tienes una tabla llamada Personas con un campo NombreCompleto,
# y quieres guardar los trigramas en una tabla nueva llamada NombreConTrigram.

# Crear conexión y cursor
conn = sqlite3.connect("mi_basedatos.db")
cursor = conn.cursor()

# Crear tablas (solo la primera vez)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Personas (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreCompleto TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS NombreConTrigram (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    NombreOriginal TEXT NOT NULL,
    Trigramas TEXT NOT NULL
)
''')

# Insertar ejemplo
cursor.execute("INSERT INTO Personas (NombreCompleto) VALUES (?)", ("Lettuce Perez",))
conn.commit()

# Obtener nombres y generar trigramas
cursor.execute("SELECT NombreCompleto FROM Personas")
nombres = cursor.fetchall()

for (nombre,) in nombres:
    trig = generar_trigramas(nombre, eliminar_duplicados=True)
    cursor.execute("INSERT INTO NombreConTrigram (NombreOriginal, Trigramas) VALUES (?, ?)", (nombre, trig))

conn.commit()
conn.close()
"""
