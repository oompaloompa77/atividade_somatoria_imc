#1. Criar um programa para monitorar sua saúde com base no cálculo do IMC (Índice de Massa Corporal).
#2. Receber a variável do peso (kg).
#3. Receber a variável de altura (m).
#4. Fazer o cálculo de IMC com base nos valores apresentados.
#5. Imprimir o valor do IMC.

peso = float(input('Insira o peso: '))
print(peso)
print('------------------------------------')
altura = float(input('Insira sua altura: '))
print(altura)
print('------------------------------------')
imc = peso / (altura**2)
print(imc)
print('----------------------------------')
if imc < 18.5 : 
    print('Você está abaixo do peso!')

elif imc <= 18.5 - 24.9: 
    print('Parabéns seu peso está normal!!')

elif imc <= 25 - 29.9 : 
    print('Infelizmente você está com sobrepeso!')

elif imc <= 30 - 34.9 : 
    print('Infelizmente você está com obesidade grau 1!')

elif imc <= 35 - 39.9 :
    print('Sinto muito, você está com obesidade grau 2!!')

else:
    print('Sinto muito, você está com obesidade grau 3!!!')




