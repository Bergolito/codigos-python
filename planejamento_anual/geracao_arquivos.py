from datetime import date, timedelta, datetime

# =========================================
# ######           funcoes           ######
# =========================================

#------------------------------------------

def monta_cabecalho_arquivo(texto):
    conteudo = []
    conteudo.append("\n=======================================================================================================================")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n# # # # # #                                                                                                   # # # # #")
    conteudo.append("\n# # # # # #                             "+texto+"                     # # # # #")
    conteudo.append("\n# # # # # #                                                                                                   # # # # #")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    conteudo.append("\n=======================================================================================================================\n\n")
    return ''.join(conteudo)

def planejamento_semanal_tarefas(ano):
    sdate = date(ano, 1, 1)  # start date
    edate = date(ano, 12, 31)  # end date
    # diferença
    delta = edate - sdate  # as timedelta
    lista_dias = []
    nome_arquivo = "Acompanhamento_Semanal_Tarefas_"+str(ano)+".txt"

    # cria po arquivo para escrita
    text_file = open(nome_arquivo, "w")

    # monta o cabecalho
    texto_cabecalho = 'Acompanhamento Semanal das Tarefas de '+str(ano)
    text_file.write(monta_cabecalho_arquivo(texto_cabecalho))

    # guarda a lista de dias do ano
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        lista_dias.append(day)

    delimitador="\n========================================================================================================================"
    tracos = "\n\n- "+"\n- "+"\n- \n\n"

    segunda_feira = ''
    sexta_feira = ''
    for d in lista_dias:
        if d.weekday() == 0:
            segunda_feira=d
            sexta_feira= segunda_feira + timedelta(days=4)
            num_semana = d.isocalendar()[1]

            print("========================================================================================================================")
            print("Semana " + str(num_semana) + " = "+str(segunda_feira.strftime('%d/%m'))+" a "+str(sexta_feira.strftime('%d/%m')))
            print("========================================================================================================================")

            linha="\nSemana " + str(num_semana) + " = "+str(segunda_feira.strftime('%d/%m'))+" a "+str(sexta_feira.strftime('%d/%m'))
            text_file.write(delimitador)
            text_file.write(linha)
            text_file.write(delimitador)
            text_file.write(tracos)
            text_file.write("\n--------------------------------------------------------------------------------")
            text_file.write("\nxx/"+str(segunda_feira.strftime('%m'))+" - descrição da despesa                                         -    00,00")
            text_file.write("\n--------------------------------------------------------------------------------\n\n")
    text_file.close()


def planejamento_semanal_alm(ano):
    sdate = date(ano, 1, 1)  # start date
    edate = date(ano, 12, 31)  # end date
    # diferença
    delta = edate - sdate  # as timedelta
    lista_dias = []
    nome_arquivo = "Acompanhamento_Semanal_ALM_"+str(ano)+".txt"

    # cria po arquivo para escrita
    text_file = open(nome_arquivo, "w")

    # monta o cabecalho
    texto_cabecalho = 'Acompanhamento Semanal das Tarefas do ALM de '+str(ano)
    text_file.write(monta_cabecalho_arquivo(texto_cabecalho))

    # guarda a lista de dias do ano
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        lista_dias.append(day)

    delimitador="\n========================================================================================================================"
    conteudo = []
    conteudo.append("\n\n------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\nSegunda-feira = 0,0 h ")
    conteudo.append("\n- Tarefa 1                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 2                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 3                                                                               - 0,00 h ")
    conteudo.append("\n------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\nTerça-feira = 0,0 h ")
    conteudo.append("\n- Tarefa 1                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 2                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 3                                                                               - 0,00 h ")
    conteudo.append("\n------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\nQuarta-feira = 0,0 h ")
    conteudo.append("\n- Tarefa 1                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 2                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 3                                                                               - 0,00 h ")
    conteudo.append("\n------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\nQuinta-feira = 0,0 h ")
    conteudo.append("\n- Tarefa 1                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 2                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 3                                                                               - 0,00 h ")
    conteudo.append("\n------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\nSexta-feira = 0,0 h ")
    conteudo.append("\n- Tarefa 1                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 2                                                                               - 0,00 h ")
    conteudo.append("\n- Tarefa 3                                                                               - 0,00 h ")
    conteudo.append("\n------------------------------------------------------------------------------------------------------------------------\n")

    segunda_feira = ''
    sexta_feira = ''
    for d in lista_dias:
        if d.weekday() == 0:
            segunda_feira=d
            sexta_feira= segunda_feira + timedelta(days=4)
            num_semana = d.isocalendar()[1]

            print("========================================================================================================================")
            print("Semana " + str(num_semana) + " = "+str(segunda_feira.strftime('%d/%m'))+" a "+str(sexta_feira.strftime('%d/%m')))
            print("========================================================================================================================")

            linha="\nSemana " + str(num_semana) + " = "+str(segunda_feira.strftime('%d/%m'))+" a "+str(sexta_feira.strftime('%d/%m'))
            text_file.write(delimitador)
            text_file.write(linha)
            text_file.write(delimitador)
            text_file.write(''.join(conteudo))
    text_file.close()

#------------------------------------------
def nome_dia_semana(weekday):
    if weekday == 0:
        return "Segunda-Feira"
    if weekday == 1:
        return "Terça-Feira"
    if weekday == 2:
        return "Quarta-Feira"
    if weekday == 3:
        return "Quinta-Feira"
    if weekday == 4:
        return "Sexta-Feira"
    if weekday == 5:
        return "Sábado"
    if weekday == 6:
        return "Domingo"

#------------------------------------------

ano = 2020
planejamento_semanal_tarefas(ano)
planejamento_semanal_alm(ano)