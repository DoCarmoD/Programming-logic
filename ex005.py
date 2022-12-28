# Pergunte ao usuário um valor e mostre o dobro, triplo e raiz quadrada desse valor 
# Ask the user for a value and show the double, triple and square root of that value

n = float(input("Digite um valor: "))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O Dobro de {n} = {dobro} \nO triplo de {n} = {triplo} \nA raiz quadrada de {n} = {raiz}')
