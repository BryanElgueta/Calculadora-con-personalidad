
import random
import colorama
from colorama import Fore, Style

# Función para sumar dos números
def sumar(a, b):
    resultado = a + b
    return resultado


# Función para restar dos números
def restar(a, b):
    resultado = a - b
    return resultado


# Función para multiplicar dos números
def multiplicar(a, b):
    resultado = a * b
    return resultado


# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return Fore.RED(
            "╔══════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
            + "¿Eh?¿Acaso no sabes que no se puede dividir entre cero? ¡Baka! No me hagas perder mi tiempo.\n"
            + "╚════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
        )
    else:
        resultado = a / b
        return resultado


# Mensajes de la imouto tsundere
mensajes_tsundere = [
    "Hmp... está bien, pero solo porque eres tú",
    "No me hagas perder mi tiempo",
    "No esperes que te ayude siempre",
    "¿Acaso no puedes hacerlo tú mismo?",
    "No creas que soy tu sirvienta personal",
    "Grrr... ¿por qué siempre tienes que pedirme ayuda?",
    "No te emociones tanto, solo estoy haciendo mi trabajo",
    "¿Es en serio? No puedo creer que me pidas eso.",
    "¡¿Qué?! ¿Cómo te atreves a decirme eso?",
    "Bueno, supongo que no tengo nada mejor que hacer...",
    "Tsk, no esperes que te trate como a un rey.",
    "No soy tu juguete, así que no me hagas enojar.",
    "¡Ugh! ¿Por qué siempre tienes que ser tan molesto?",
    "Hmph, tú no eres el único que tiene cosas que hacer, ¿sabes?",
    "Si quieres que te ayude, deberías decir 'por favor' primero, ¿no crees?",
]

# Función para imprimir un mensaje tsundere aleatorio
def mensaje_tsundere():
    mensaje = random.choice(mensajes_tsundere)
    return mensaje


# Función principal de la calculadora tsundere
def calcular():
    # Imprime un mensaje de bienvenida
    print(
        "\033[1m\033[3m"
        + Fore.LIGHTMAGENTA_EX
        + "╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + " No es que me importe mucho, pero por fin llegaste, Onii-chan... ¿Por qué tardaste tanto? Ya te estaba esperando, pero no esperes que te trate con demasiada dulzura, ¿eh?\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝",
    )


# Llama a la función calcular() para imprimir el mensaje de bienvenida
calcular()

# Pide al usuario que ingrese una operación
operacion = input(
    "\033[1m\033[3m"
    + Fore.LIGHTMAGENTA_EX
    + "╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
    + " ¿No puedes hacer nada sin mi ayuda, Onii-chan? Elige: suma (+), resta (-), multiplicación (*, x) o división (/, d). No me hagas repetirlo, baka.\n"
    + "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    + Style.BRIGHT
    + Fore.WHITE
)

    # Pide al usuario que ingrese dos números y la operación a realizar
while True:
        try:
            num1 = float(
                input(
                    Fore.MAGENTA
                    + "╔═════════════ »•» 🌺 «•« ═╗\n"
                    + " Ingresa el primer número:\n"
                    + "╚════════════ »•» 🌺 «•« ══╝\n"
                    + Style.BRIGHT
                    + Fore.WHITE
                )
            )
            break
        except ValueError:
            print(
                "\033[1m\033[3m"
                + Fore.RED
                + "╔══════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
                + " ❌¡Baka! ¿Acaso no sabes lo que es un número? Ingresa un número válido.\n"
                + "╚═════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
            )
while True:
        try:
            num2 = float(
                input(
                    Fore.MAGENTA
                    + "╔═════════════ »•» 🌺 «•« ═╗\n"
                    + " Ingresa el segundo número:\n"
                    + "╚════════════ »•» 🌺 «•« ══╝\n"
                    + Style.BRIGHT
                    + Fore.WHITE
                )
            )
            break
        except ValueError:
            print(
                "\033[1m\033[3m"
                + Fore.RED
                + "╔════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
                + " ❌¡Baka! ¿Acaso no sabes que un número es algo básico? Ingresa un número válido.\n"
                + "╚═══════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
            )


# Comprueba si la entrada del usuario es una operación válida
operaciones_validas = {
    "s", "S", "Sumar", "Suma", "sumar", "suma", "+",
    "r", "R", "Restar", "restar", "Resta", "resta", "-",
    "m", "multiplicación", "multiplicacion", "*", "x",
    "d", "división", "/", "division"
}

while operacion.lower() not in operaciones_validas:

    # Si la entrada no es válida, muestra un mensaje de error
    print(
        "\033[1m\033[3m"
        + Fore.RED
        + "╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + " ❌ ¡Baka! Solo se permiten las operaciones suma (+), resta (-), multiplicación (*, x) y división (/, d). Ingresa una operación correcta.\n"
        + "╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝"
    )
    operacion = input(
        "\033[1m\033[3m"
        + Fore.LIGHTMAGENTA_EX
        + "╔════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + " Introduce una operación válida (suma, resta, multiplicación o división):\n"
        + "╚═══════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
        + Style.BRIGHT
        + Fore.WHITE
    )
  


# Realiza la operación correspondiente y muestra el resultado
if (
    operacion == "sumar"
    or operacion == "Sumar"
    or operacion == "+"
    or operacion == "s"
    or operacion == "S"
    or operacion == "Suma"
    or operacion == "suma"
):
    resultado = sumar(num1, num2)
    print(
        Fore.MAGENTA
        + "╔════════ »•» 🌺 «•« ═╗\n"
        + "El resultado es:"
        + Style.BRIGHT
        + Fore.WHITE
        + str(resultado)
        + "\n"
        + "╚═══════ »•» 🌺 «•« ══╝\n"
    )
    # imprime un mensaje tsundere al azar
    print(
        "\033[1m\033[3m"
        + Fore.YELLOW
        + "╔════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + mensaje_tsundere()
        + "\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    )

elif (
    operacion == "resta"
    or operacion == "-"
    or operacion == "restar"
    or operacion == "Restar"
    or operacion == "r"
    or operacion == "R"
    or operacion == "Resta"
):
    resultado = restar(num1, num2)
    print(
        Fore.MAGENTA
        + "╔════════ »•» 🌺 «•« ═╗\n"
        + "El resultado es:"
        + Style.BRIGHT
        + Fore.WHITE
        + str(resultado)
        + "\n"
        + "╚═══════ »•» 🌺 «•« ══╝\n"
    )
    # imprime un mensaje tsundere al azar
    print(
        "\033[1m\033[3m"
        + Fore.YELLOW
        + "╔════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + mensaje_tsundere()
        + "\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    )

elif (
    operacion == "multiplicacion"
    or operacion == "*"
    or operacion == "x"
    or operacion == "m"
    or operacion == "M"
    or operacion == "multiplicación"
    or operacion == "Multiplicación"
    or operacion == "Multiplicacion"
):
    resultado = multiplicar(num1, num2)
    print(
        Fore.MAGENTA
        + "╔════════ »•» 🌺 «•« ═╗\n"
        + "El resultado es:"
        + Style.BRIGHT
        + Fore.WHITE
        + str(resultado)
        + "\n"
        + "╚═══════ »•» 🌺 «•« ══╝\n"
    )
    # imprime un mensaje tsundere al azar
    print(
        "\033[1m\033[3m"
        + Fore.YELLOW
        + "╔════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + mensaje_tsundere()
        + "\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    )

elif (
    operacion == "division"
    or operacion == "/"
    or operacion == "d"
    or operacion == "D"
    or operacion == "división"
    or operacion == "División"
    or operacion == "Division"
):
    resultado = dividir(num1, num2)
    print(
        Fore.MAGENTA
        + "╔════════ »•» 🌺 «•« ═╗\n"
        + "El resultado es:"
        + Style.BRIGHT
        + Fore.WHITE
        + str(resultado)
        + "\n"
        + "╚═══════ »•» 🌺 «•« ══╝\n"
    )
    # imprime un mensaje tsundere al azar
    print(
        "\033[1m\033[3m"
        + Fore.YELLOW
        + "╔════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + mensaje_tsundere()
        + "\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    )

else:
    print(
        "\033[1m\033[3m"
        + Fore.RED
        + "╔════════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ═╗\n"
        + " ❌¡Baka! ¿En qué estás pensando? Esa no es una operación válida. Ingresa una operación correcta.\n"
        + "╚═══════════════════════════════════════════════════════════════════════════════════ »•» 🌺 «•« ══╝\n"
    )





