def palavras(elem):
     return elem.upper(), elem.lower(), len(elem)

texto = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

for op in (map(palavras, texto)):
    print(op)