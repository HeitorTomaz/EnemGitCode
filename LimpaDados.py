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

linha0 = ['id', 'Geral', 'redacao', 'matematica', 'linguagens', 'humanas' ,'natureza']
row2 = [0,0,0,0,0,0,0]

with open("MICRODADOS_ENEM_2014.csv", "rb") as fp_in, open( "./Dados/Medias.csv", "wb" ) as fp_out:
	reader = csv.reader(fp_in, delimiter=",")
	writer = csv.writer(fp_out, delimiter=",")
	for row in reader:
		total += 1
		if indice == 0: #pula a linha do indice
			writer.writerow(linha0)
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
	##################################################################################################
		if row[colDados['comparecimentoMatematica']] == row[colDados['comparecimentoLinguagens']] == row[colDados['comparecimentoHumanas']] == row[colDados['comparecimentoNatureza']] == '1': #verifica se aluno compareceu a prova
			# Aqui comeca a separar os dados
			#print table[0][int(row[colDados['idade']])][colTable['quantidade']]
			row2[0] = indice
			row2[1] = 0
			for disciplina in disciplinas:
				row2[1] += float(row[colDados[disciplina]])
				row2[colTable[disciplina]] = float(row[colDados[disciplina]])
				row2[colTable[disciplina]] = float("%.2f" % row2[colTable[disciplina]]) #seta pra 2 casas decimais
			row2[1] = row2[1]/5
			row2[1] = float("%.2f" % row2[1]) #seta pra 2 casas decimais
			#print row2
			writer.writerow(row2)
		else:
			faltou +=1

print 'Total de alunos inscritos: '
print total
print
print 'Alunos faltosos: '
print faltou
print
print 'Compareceram: '
print total - faltou
print

