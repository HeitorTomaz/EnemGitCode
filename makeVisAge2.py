import csv
import math
indice = 0
faltou = 0
total = 0
idadeMinima = 16
idadeMaxima = 50

colDados = {'estado':61, 'matematica':73, 'comparecimentoMatematica':65, 'linguagens':72 , 'comparecimentoLinguagens':64,
	'humanas':71, 'comparecimentoHumanas':63, 'natureza':70,'comparecimentoNatureza':62, 'redacao':89, 'statusRedacao':83,
	'idade':15, 'tipoEscola':12, 'tipoEscolaQuestionario':124, 'preVestibular':137}

estados = ["geral"]
boolean = 0
table = [ [ ['a' if j == 0 else (j + idadeMinima -2) if i == 0 else 0 for i in range(8)] for j in range(idadeMaxima - idadeMinima + 3) ] for k in range(30) ]

colTable = {'idade':0 ,'quantidade':1 ,'redacao':2 ,'matematica':3 ,'linguagens':4 ,'humanas':5 ,'natureza':6, 'geral':7}
linha1 = ['idade','quantidade', 'redacao', 'matematica', 'linguagens', 'humanas', 'natureza', 'geral']
disciplinas = ['linguagens', 'natureza', 'humanas', 'matematica', 'redacao']

#estad = ["SP"	"MG"		"BA"		"RJ"		"CE"		"DF"		"RS"		"PI"		"MS"		"PR"		"GO"		"AC"		"PE"		MA		AL		PA		MT		ES		AM		RO		PB		AP		RN		SC		RR		TO	SE

print table[0][0][0] #a
print table[0][0][1] #a
print table[0][1][0] #1
print table[1][0][0] #a
print table[1][1][1] #0

with open("MICRODADOS_ENEM_2014.csv", "rb") as fp_in:
	reader = csv.reader(fp_in, delimiter=",")
	for row in reader:
		total += 1
		if indice == 0: #pula a linha do indice
			i = 0
			total = total - 1
			for ii in range(len(table)):
				i = 0
				for texto in linha1:
					table[ii][0][i] = texto #adiciona primeira linha
					i += 1
			indice +=1
			continue
		try:
			float(row[colDados['idade']])
		except:
		#	ex += 1
		#	print ex
			continue
		indice += 1
		indiceEstados = 0
		for state in estados: #descobre o Estados
			if not row[colDados['estado']]:
				indiceEstados = 29
				break
			if state == row[colDados['estado']]:
				boolean = 1
				break
			else:
				indiceEstados += 1
				pass
		if boolean == 0: #adiciona Estado
			estados.append(row[colDados['estado']]);
		boolean = 0
		#print table[0][0][5] #humanas
		indice += 1
	##################################################################################################
		if row[colDados['comparecimentoMatematica']] == row[colDados['comparecimentoLinguagens']] == row[colDados['comparecimentoHumanas']] == row[colDados['comparecimentoNatureza']] == '1': #verifica se aluno compareceu a prova
			# Aqui comeca a separar os dados
			#print table[0][int(row[colDados['idade']])][colTable['quantidade']]
			if (int(row[colDados['idade']]) >= idadeMinima ) and (int(row[colDados['idade']]) <idadeMaxima):
				table[0][int(row[colDados['idade']]) - idadeMinima + 2][colTable['quantidade']] += 1
				table[indiceEstados][int(row[colDados['idade']]) - idadeMinima + 2][colTable['quantidade']] += 1
				for disciplina in disciplinas:	#operando sobre as disciplinas
					table[0][int(row[colDados['idade']]) - idadeMinima + 2][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
					table[indiceEstados][int(row[colDados['idade']]) - idadeMinima + 2][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
			if int(row[colDados['idade']]) <idadeMinima :
				table[0][1][colTable['quantidade']] += 1
				table[indiceEstados][1][colTable['quantidade']] += 1
				for disciplina in disciplinas:	#operando sobre as disciplinas
					table[0][1][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
					table[indiceEstados][1][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
			if int(row[colDados['idade']]) >= idadeMaxima :
				table[0][idadeMaxima - idadeMinima + 2][colTable['quantidade']] += 1
				table[indiceEstados][idadeMaxima - idadeMinima + 2][colTable['quantidade']] += 1
				for disciplina in disciplinas:	#operando sobre as disciplinas
					table[0][idadeMaxima - idadeMinima + 2][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno
					table[indiceEstados][idadeMaxima - idadeMinima + 2][colTable[disciplina]] += float(row[colDados[disciplina]]) #adiciona a nota do aluno

		else:
			faltou +=1


print table[1]
indiceEstados = 0
for nomeEstados in estados:	
	with open( "./estados/" + nomeEstados + ".csv", "wb" ) as fp_out:
		writer = csv.writer(fp_out, delimiter=",")
		indice =  0
		for row2 in table[indiceEstados]:
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
	indiceEstados +=1

print 'Total de alunos inscritos: '
print total
print
print 'Alunos faltosos: '
print faltou
print
print 'Compareceram: '
print total - faltou
print

