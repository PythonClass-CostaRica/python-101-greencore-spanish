operando_uno = '234 '
operando_dos = '23 '

print(type(operando_uno))
print(type(operando_dos))
resultado = operando_uno + ' ' +  operando_dos
print(resultado)
print(type(resultado))

# Operadores aritméticos
operando_a = 123783
operando_b = 2892

print(operando_a + operando_b)  # Suma
print(operando_a * operando_b)  # Multiplicación
print(operando_a - operando_b)  # Resta

# División

print(7 / 2) 
print(7 // 2)
print(7 % 2)

print(operando_a % operando_b)

# Potencias
# print(operando_a ** operando_b) # a elevado a la potencia (b) aˆb
print(operando_a ** (1/2))  # Raiz cuadrada de operando a

a = 5
b = 3
c = 2

# Cáculo de un discriminante
discriminante = (b**2) - (4*a*c)
print(discriminante)

# Cadenas
texto = 'Hola este , un: mensaje!'

print(ord(texto[0]))
print(chr(73))
print(texto[5:9][::-1].capitalize())
print(texto.split())
print(texto.replace(' ', ''))

texto2 = texto
texto2 = texto2.upper()
print(texto)
print(texto2)













