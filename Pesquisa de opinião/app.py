excelente = 0
ruim = 0
for i in range (1,51):
    nome = input("Digite seu nome:")
    idade = input ("Digite sua idade:")
    opiniao_do_entrevistado = int(input("De 1 a 3, qual a sua nota para o atendimento:\n"
"1.Excelente\n"
"2.Bom\n"
"3.Ruim\n>"))
    if opiniao_do_entrevistado ==1:
        excelente += 1
    if opiniao_do_entrevistado ==3:
        ruim += 1
print ("Quantidade de notas Excelente:", excelente)
print ("Quantidade de notas Ruim:", ruim)

#Teste com a opinião de 10 entrevistados
#for i in range (1,11):
#Versão final do sistem com 50 entrevistados 
#for i in range (1,51):