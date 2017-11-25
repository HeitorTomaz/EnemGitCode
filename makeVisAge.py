import csv
import math
indice = 0
faltou = 0
total = 0
colDados = {'estado':61, 'matematica':73, 'comparecimentoMatematica':65, 'linguagens':72 , 'comparecimentoLinguagens':64,
	'humanas':71, 'comparecimentoHumanas':63, 'natureza':70,'comparecimentoNatureza':62, 'redacao':89, 'statusRedacao':83,
	'idade':15, 'tipoEscola':12, 'tipoEscolaQuestionario':124, 'preVestibular':137}

estados = []
boolean = 0
table = [ [ 'a' if j == 0 else j if i == 0 else 0 for i in range(8) ] for j in range(100) ]

colTable = {'idade':0 ,'quantidade':1 ,'redacao':2 ,'matematica':3 ,'linguagens':4 ,'humanas':5 ,'natureza':6, 'geral':7}
linha1 = ['idade','quantidade', 'redacao', 'matematica', 'linguagens', 'humanas', 'natureza', 'geral']
disciplinas = ['linguagens', 'natureza', 'humanas', 'matematica', 'redacao']

with open("MICRODADOS_ENEM_2014.csv", "rb") as fp_in, open("MEDIAS_VIS_AGE.csv", "wb") as fp_out:
	reader = csv.reader(fp_in, delimiter=",")
	writer = csv.writer(fp_out, delimiter=",")
	for row in reader:
		total += 1
		if indice == 0: #pula a linha do indice
			i = 0
			total = total - 1
			for texto in linha1:
				table[0][i] = texto #adiciona primeira linha
				i += 1
			indice +=1
			continue
		try:
			float(row[colDados['idade']])
		except:
			continue
		indice += 1
	##################################################################################################
		if row[colDados['comparecimentoMatematica']] == row[colDados['comparecimentoLinguagens']] == row[colDados['comparecimentoHumanas']] == row[colDados['comparecimentoNatureza']] == '1': #verifica se aluno compareceu a prova
			# Aqui comeca a separar os dados
			table[int(row[colDados['idade']])][colTable['quantidade']] += 1
			for disciplina in disciplinas:	#operando sobre as disciplinas
				table[int(row[colDados['idade']])][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
		else:
			faltou +=1


	print
	indice =  0
	for row2 in table:
		if indice == 0:
			indice += 1
			writer.writerow(row2)
			continue
		if row2[colTable['quantidade']]: #verifica se ha alunos daquela idade
			for disciplina in disciplinas:
				row2[colTable['geral']] += row2[colTable[disciplina]]
				row2[colTable[disciplina]] = row2[colTable[disciplina]] / row2[colTable['quantidade']] #computa a media da idade
				row2[colTable[disciplina]] = float("%.2f" % row2[colTable[disciplina]]) #seta pra 2 casas decimais
			row2[colTable['geral']] = row2[colTable['geral']] / (row2[colTable['quantidade']]*5)
			row2[colTable['geral']] = float("%.2f" % row2[colTable['geral']])
		indice += 1

		writer.writerow(row2) #escreve a linha

print 'Total de alunos inscritos: '
print total
print
print 'Alunos faltosos: '
print faltou
print
print 'Compareceram: '
print total - faltou
print

