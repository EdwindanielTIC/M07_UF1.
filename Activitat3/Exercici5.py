Scanner = input("introduce la frase ")

frase = Scanner.replace(" ","")

resultado = ""

print("frase sin elimnar caracteres = "+frase)

for x in frase:
    if x not in resultado: ## verifica si sale por primera vez el caracter, por lo que es un caracter unico
        resultado += x
        
print(resultado)




# replace() se utiliza para remplazar los espacios con una cadena vacia ejemplo hola mundo = holamundo
# para reducir los espacios adicionales se utilizar el split y join --> " hola ,  como estas " == "hola, como estas"   : join(frasecualquier.split())
# strip() quita los espacios al inicio y al final 