def primo(n):
    try:
        n = int(n)
        if n <= 1:
            return "No es primo"
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return "No es primo"
        return "Es primo"
    
    except ValueError:
        return "Error: El valor ingresado no es un número válido."


print(primo(10))
