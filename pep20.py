""" python import this """

FRASE = "hola noa canoa, ¿cómo estás?"
x = FRASE.startswith("hola")
y = FRASE.endswith("estás?")

print(x)
print(y)


def saludo():
    """
    funcion que retorna un saludo
    """
    return "saludo"


print(saludo())
