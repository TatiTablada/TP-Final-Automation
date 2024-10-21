import math

def ecuacion_cuadratica(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No hay raíces válidas"
    return ((-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))
