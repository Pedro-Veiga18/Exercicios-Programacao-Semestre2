
aulas = ["A1", "A2", "A3", "A4", "A5"]
presencas = {
 "Gigi": ["P", "P", "P", "P", "P"],
 "Rafa": ["P", "F", "F", "P", "F"],
 "Wesley": ["P", "P", "F", "P", "P"],
 "Balela": ["F", "F", "P", "F", "P"]
}

def operacaoPresenca(presencas, aulas) :
        realatorio = {
            "por_aluno" : { 
         },
         "aula_com_mais_faltas": "",
         "melhor_presenca" : "",
         "mais_faltas" : "",
         "presenca_media_turma" : 0 
        }
        melhor_presenca = 0
        mais_faltas = float("inf")
        presenca_media_turma = 0
        faltas_por_aula = [0] * len(aulas)

        for chave, valor in presencas.items():
                F = 0
                P = 0
                perc = 0
                situacao = ""
                
                for i in range(len(valor)): 
                        if valor[i] == "P" :
                                P+=1
                        else: 
                                F += 1
                                faltas_por_aula[i] += 1

                        perc = (P / len(valor)) * 100

                        
                        
                        if perc >= 75.0 :
                                situacao = "APROVADO"
                        else: 
                                situacao = "REPROVADO"
                        
                        if perc > melhor_presenca:
                                melhor_presenca = perc
                                realatorio["melhor_presenca"] = chave
                        if perc < mais_faltas:
                                realatorio["mais_faltas"] = chave 
                        else: continue

                presenca_media_turma = presenca_media_turma + perc
                        

                realatorio["por_aluno"][chave] = {
                        "P" : P,
                        "F" : F,
                        "perc" : perc,
                        "situacao" : situacao
                }
        indice_max = faltas_por_aula.index(max(faltas_por_aula))
        realatorio["aula_com_mais_faltas"] = aulas[indice_max]       
        realatorio["presenca_media_turma"] = presenca_media_turma / len(presencas)

        
        return realatorio

relatorio = operacaoPresenca(presencas, aulas)

def exibirRelatorio(relatorio) :
    for chave, valor in relatorio.items():
        print(f'{chave} --> {valor}')
        print()

exibirRelatorio(relatorio)