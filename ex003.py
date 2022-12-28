#Dissecando uma variável
#Dissecting a variable


a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaços? ",a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
