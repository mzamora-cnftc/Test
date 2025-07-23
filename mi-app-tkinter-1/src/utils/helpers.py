def validar_entrada(entrada, tipo):
    if tipo == 'texto':
        return isinstance(entrada, str) and bool(entrada.strip())
    elif tipo == 'numero':
        try:
            float(entrada)
            return True
        except ValueError:
            return False
    return False

def formatear_datos(datos):
    return [str(dato).strip() for dato in datos]