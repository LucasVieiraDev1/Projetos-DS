# Pedir o nome do aparelho
nome = input("Digite o nome do aparelho: ")
# Pedir a potência do aparelho utilizdo
potencia = float(input("Digite a potência do aparelho em Watts: "))
# Tempo de uso diário do aparelho
horasDia = float(input("Tempo de uso diário do aparelho em horas: "))
# Calcular consumo mensal
consumo = (potencia * horasDia * 30) / 1000
# Calcular o gasto mensal estimado
custo = consumo * 0.75
# Mostrar resultado com o gasto mensal
print(f"Aparelho: {nome}, consumo estimado: {consumo} kWh/mês e o custo estimado é de R$ {custo}")
