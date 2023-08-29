"""crie um programa que peça um numero e mostre o seu sucessor e antecessor

crie um programa que leia dois numeros e exiba a soma dos dois numeros, a subtracao, multiplicacao e divisao

crie um programa que leia dois numeros e que exiba True se o primeiro numero for maior que o primeiro e False se o primeiro numero for menor ou igual ao segundo numero

crie um programa que leia uma temperatura em celsius e a converta para fahrenheit"""

#num = int(input("insira um numero: "))
# antecessor = num -1
# sucessor = num +1

# print("o sucessor do seu numero é ", sucessor) 
# print("o antecessor do seu numero é ", antecessor) 

# print(f'o {num} tem como seu sucessor {num +1} e de antecessor {num-1}')


# num = int(input("insira um numero: "))
# num2 = int(input("insira mais um numero: ")) 
# somar = num + num2 
# subtracao = num - num2
# multiplicacao = num * num2
# divisao = num / num2 
# print("a soma desses dois nùmeros é igual a", somar)
# print(" a subtração desses dois números é igual a", subtracao)
# print(" a multiplicação desses dois números é igual a", multiplicacao)
# print(" a divisão desses dois números é igual a", divisao)

# num = int(input("insira um numero: "))
# num2 = int(input("insira mais um numero: "))
# num, num2
# if num > num2: 
#     print(True,'o primeiro  numero é maior que o segundo')
# else:
#     print(False,'o segundo  numero é maior que o primeiro')
# temp= float(input("digite a temperatura:")) 
# conversor=(temp*1.8)+ 32
# print(conversor)
 #print(" a temperatura de hoje em fahrenheit é:",conversor)
velocidade = float(input("digite sua velocidade: "))

#if velocidade>=80:
#   print("você foi multado") 
#   multa = (velocidade-80)*7
#   print ("sua multa foi de R$:", multa)
#else:
#   print("você é um motorista responsável: )")     

def multa():
    velocidade = float(input("digite sua velocidade: "))

    if velocidade>=80:
        print("você foi multado") 
        multa = (velocidade-80)*7
        print ("sua multa foi de R$:", multa)
    else:
        print("você é um motorista responsável: )")   
