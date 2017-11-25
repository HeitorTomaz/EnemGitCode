import csv
import math
indice = 0
indiceDisciplinas = 0
faltou = 0
total = 0
colDados = {'estado':61, 'matematica':73, 'comparecimentoMatematica':65, 'linguagens':72 , 'comparecimentoLinguagens':64,
	'humanas':71, 'comparecimentoHumanas':63, 'natureza':70,'comparecimentoNatureza':62, 'redacao':89, 'statusRedacao':83,
	'idade':15, 'tipoEscola':12, 'tipoEscolaQuestionario':124, 'preVestibular':137}

estados = []
boolean = 0
table = [ [ str(i) if i == 0 or j == 0 else 0 for i in range(100) ] for j in range(5*29) ]

#colTable = {'estado':0, 'quantidadeAlunos': 1, 'matematica':5, 'linguagens':4, 'humanas':3, 'natureza':2, 'redacao':6,
#	'quantidadeRedacoes':7, 'quantidadeRedacoes0':8, 'quantidade1000':9, 'idade':10, 'notaIdade':11, 'idade1':12,
#	'notaIdade1':13,'idade2':14, 'notaIdade2':15, 'idade3':16, 'notaIdade3':17, 'idade4':18, 'notaIdade4':19, 'escolaFederal':20,
#	'mediaFederal':21, 'escolaEstadual':22, 'mediaEstadual':23, 'escolaMunicipal':24,'mediaMunicipal':25, 'escolaPrivada':26,
#	'mediaPrivada':27,'escolaPublicaQuestionario':28, 'mediaPublicaQuestionario':29,'escolaPrivadaQuestionario':30, 'mediaPrivadaQuestionario':31,
#	'comPreVest':32, 'mediaComPreVest':33, 'semPreVest':34, 'mediaSemPreVest':35}

#linha1 = ['estado', 'quantidade de alunos', 'Natureza','Humanas' ,'Linguagens' ,'Matematica' ,'Redacao','Recacoes corrigidas',
#	'Redacoes zeradas','Redacoes 1000','ate 14 anos', 'media ate 14','14 - 19', 'Media 14 - 19', '20 - 24', 'Media 20 - 24', '25 - 29',
#	'Media 25 - 29', 'acima de 29', 'Media acima de 29', 'E. Federal', 'Media Federal', 'E. Estadual', 'Media Estadual', 'E. Municipal',
#	'Media Municipal', 'E. Privada', 'Media Privada', 'E. Publica Questionario', 'Media Publica Questionario', 'E. Privada Questionario', 
#	'Media Privada Questionario', 'Com Pre Vest','Media Com Pre vest', 'Sem Pre Vest', 'Media Sem Pre Vest']


#print table[0]
#
#	Formatacao utilizada: 
#	colunas = estados, clusterizados por disciplina 
#	linhas  = idades
#
#

disciplinas = ['linguagens', 'natureza', 'humanas', 'matematica']

with open("MICRODADOS_ENEM_2014.csv", "rb") as fp_in, open("MEDIAS_MICRODADOS.csv", "wb") as fp_out:
	reader = csv.reader(fp_in, delimiter=",")
	writer = csv.writer(fp_out, delimiter=",")
	for row in reader:
		total += 1
		if indice == 0: #pula a linha do indice
			i = 0
			total = total - 1
			for texto in linha1:
#				table[0][i] = texto #adiciona primeira linha
				i += 1
			#print row[137]
			indice +=1
			continue
		try:
			float(row[colDados['idade']])
		except:
		#	ex += 1
		#	print ex
			continue
		indice += 1
		indiceEstados = 1
		for state in estados: #descobre o Estados
			if not row[colDados['estado']]:
				break
			if state == row[colDados['estado']]:
				boolean = 1
				break
			else:
				indiceEstados += 1
		if boolean == 0: #adiciona Estado
			estados.append(row[colDados['estado']]);
			table[indiceEstados][colTable['estado']] = row[colDados['estado']]
		boolean = 0
	###################################################################################################
		if row[colDados['comparecimentoMatematica']] == row[colDados['comparecimentoLinguagens']] == row[colDados['comparecimentoHumanas']] == row[colDados['comparecimentoNatureza']] == '1': #verifica se aluno compareceu a prova
			






		else:
			faltou +=1


	print
	indice =  0
	for row2 in table:
		if indice == 0:
			indice += 1
			writer.writerow(row2)
			continue
		if row2[colTable['quantidadeAlunos']]: #verifica se ha alunos daquele Estado
			for disciplina in disciplinas:
				row2[colTable[disciplina]] = row2[colTable[disciplina]] / row2[colTable['quantidadeAlunos']] #computa a media do Estado
				row2[colTable[disciplina]] = float("%.2f" % row2[colTable[disciplina]]) #seta pra 2 casas decimais
			row2[colTable['redacao']] = row2[colTable['redacao']] / row2[colTable['quantidadeRedacoes']] #computa a media do Estado
			row2[colTable['redacao']] = float("%.2f" % row2[colTable['redacao']]) #seta pra 2 casas decimais

			for indice2 in range(1, 6):
				if  row2[colTable['idade'] + 2 * indice2 - 1] != 0:
					row2[colTable['idade'] + 2 * indice2 - 1] = row2[colTable['idade'] + 2 * indice2 - 1]/row2[colTable['idade'] + 2 * indice2 - 2]
					row2[colTable['idade'] + 2 * indice2 - 1] = float("%.2f" %row2[colTable['idade'] + 2 * indice2 - 1])
			for indice2 in range(1, 5):
				if  row2[colTable['mediaFederal'] + 2 * indice2 - 3] != 0:
					row2[colTable['mediaFederal'] + 2 * indice2 - 2] = row2[colTable['mediaFederal'] + 2 * indice2 - 2]/row2[colTable['mediaFederal'] + 2 * indice2 - 3]
					row2[colTable['mediaFederal'] + 2 * indice2 - 2] = float("%.2f" %row2[colTable['mediaFederal'] + 2 * indice2 - 2])
			for indice2 in range(0, 2):
				if  row2[colTable['escolaPublicaQuestionario'] + 2 * indice2] != 0:
					row2[colTable['escolaPublicaQuestionario'] + 2 * indice2 +1] = row2[colTable['escolaPublicaQuestionario'] + 2 * indice2 +1]/row2[colTable['escolaPublicaQuestionario'] + 2 * indice2]
					row2[colTable['escolaPublicaQuestionario'] + 2 * indice2 +1] = float("%.2f" %row2[colTable['escolaPublicaQuestionario'] + 2 * indice2 +1])
			for indice2 in range(0, 2):
				if  row2[colTable['comPreVest'] + 2 * indice2] != 0:
					row2[colTable['comPreVest'] + 2 * indice2 +1] = row2[colTable['comPreVest'] + 2 * indice2 +1]/row2[colTable['comPreVest'] + 2 * indice2]
					row2[colTable['comPreVest'] + 2 * indice2 +1] = float("%.2f" %row2[colTable['comPreVest'] + 2 * indice2 +1])


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

