# %% data to decision 
def analizar(lecturas, limite_max):
    # DATO: la última lectura. Pista: el índice -1 es el último
    dato = lecturas[-1]

    # INFORMACIÓN: "Temperatura almacén: X°C (límite: Y°C)"
    informacion = f"Temperatura almacén: {dato}°C (límite: {limite_max}°C)"

    # CONOCIMIENTO: ¿cuántas lecturas superan el límite, y va subiendo?
    lecturas_fuera = len([x for x in lecturas if x > limite_max])
    tendencia = "subiendo" if lecturas[-1] > lecturas[0] else "estable"       # "subiendo" si la última > la primera, si no "estable"

    # DECISIÓN: si dato > límite Y subiendo → "URGENTE: revisar refrigeración"
    #           si dato > límite             → "Alerta: monitorizar próxima hora"
    #           si no                        → "Normal, sin acción"
    if dato > limite_max and tendencia == "subiendo":
        decision = "URGENTE: revisar refrigeración"
    elif dato > limite_max:
        decision = "Alerta: monitorizar próxima hora"
    else:
        decision = "Normal, sin acción"
        

    # --- No toques ---
    print(f"Dato: {dato}")
    print(f"Info: {informacion}")
    print(f"Conocimiento: {tendencia}, fuera={lecturas_fuera}")
    print(f"Decisión: {decision}")
    print("")


# --- No toques: tres almacenes distintos ---
analizar([4.2, 4.5, 5.1, 6.8, 7.9, 9.1], 8.0)
analizar([9.5, 9.0, 8.8, 8.6, 8.4, 8.2], 8.0)
analizar([6.1, 5.8, 6.0, 5.9, 6.2, 5.7], 8.0)

# %% Nule vs empty
# 200 clientes generados por el bucle. Contarlos a mano no es viable:
# hay que escribir el código.
clientes = []
for i in range(200):
    if i % 7 == 0:
        email = None                      # no tenemos el dato
    elif i % 5 == 0:
        email = ""                        # el campo existe y está vacío
    else:
        email = f"cliente{i}@mail.com"
    clientes.append({"nombre": f"Cliente {i}", "email": email})

# Cuenta cada grupo. None y "" NO son lo mismo.
#   · válido -> tiene un email de verdad
#   · nulo   -> es None
#   · vacío  -> es la cadena ""
# Pista: len([c for c in clientes if ...])
email_valido = 0
email_nulo = 0
email_vacio = 0

# --- No toques: la comprobación.
#     La clave va del revés para que no se lea de un vistazo. ---
CLAVE = "43,92,731"
correctos = [int(x) for x in CLAVE[::-1].split(",")]

aciertos = 0
for etiqueta, mio, bueno in zip(["validos", "nulos", "vacios"],
                                [email_valido, email_nulo, email_vacio], correctos):
    if mio == bueno:
        print(f"  OK    {etiqueta}")
        aciertos += 1
    else:
        print(f"  FALLO {etiqueta}: pusiste {mio}")
print(f"\nAciertos: {aciertos}/3")
# %%
