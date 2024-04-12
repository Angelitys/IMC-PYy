'''    - Nome   - Altura (cm)
   - Peso (kg)
   Com base nestes dados realize o calculo para 
  descobrir qual o IMC (indice de massa corporea)da pessoa.
    Para o calculo utilize a tabela padrão do IMC.
    abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani)
    entre 18,6 e 24,9 - Peso Ideal (Para Bens)
    entre 25,0 e 29,9 - Sobrepeso
    entre 30,0 e 34,9 - Obesidade Grau 1
    entre 35,0 e 39,9 - Obesidade Grau 2
    acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)
    formula: IMC = peso / altura²'''

nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura em centímetros: "))
peso = float(input("Informe seu peso em quilogramas: "))
 
imc = peso / (altura / 100) ** 2

if imc < 18.5:
    classificacao = "Abaixo do Peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso Ideal (Parabéns)"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade Grau 1"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade Grau 2"
else:
    classificacao = "Obesidade Grau 3"

texto = f"""
Olá, {nome}!
Seu IMC é: {imc:.2f}
Classificação: {classificacao}
"""
print(texto)




