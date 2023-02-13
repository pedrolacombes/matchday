# -*- coding: utf-8 -*-
"""Codigo_MVP_Matchday

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10HbU1kZl20gJgK8-MBIZeuppj6aZRfCV
"""

# Importando bibliotecas para desenhar o campo
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mat
import streamlit as st
import cv2
import moviepy.editor as moviepy

# Puxando o arquivo com a base de passes

sheet_id = '15Zkt-YrhKGC3JKdPhGl5tjQhaeCfihJiGUev1DKP52o'
sheet_name = 'Geral'
url = 'https://docs.google.com/spreadsheets/d/'+sheet_id+'/gviz/tq?tqx=out:csv&sheet='+sheet_name
data = pd.read_csv(url)


# transformando a tabela em dataframe

my_df = pd.DataFrame(data)
my_df = my_df[my_df['Index_Evento'] != 'Sem valor']

# declarando as 3 colunas do aplicativo

tab1, tab2, tab3, tab4 = st.tabs(['Tabela Geral','Evolucao','Mapas','Videos'])

# montando pagina do tabelao

with tab1:

  # Criar lista com lista única das partidas
  Partidas = my_df.Index_Partida.unique()
  Partidas = Partidas.tolist()
  Partidas.sort()

  # Definindo dicionário para stats da coluna nome_ato
  stats_nome_ato = ['Passe', 'Finalização', 'Corte', 'Cartão Amarelo', 'Cartão Vermelho', 'Bloqueio de chute',
                    'Desarme', 'Drible', 'Falta cometida', 'Falta sofrida', 'Perda de posse']

  dicionario_nome_ato = {
    stat: {Partida: sum((my_df.Nome_Ato == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas} for stat
    in stats_nome_ato}

  print(dicionario_nome_ato)

  # Definindo dicionário para stats da coluna finalizacao_outcome
  stats_finalizacao_outcome = ['Finalização no gol', 'Finalização para fora', 'Finalização bloqueada']

  dicionario_finalizacao_outcome = {
    stat: {Partida: sum((my_df.Nome_Finalizacao_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in
           Partidas} for stat in stats_finalizacao_outcome}

  print(dicionario_finalizacao_outcome)

  # Definindo dicionário para stats da coluna pass_outcome
  stats_pass_outcome = ['Passe Certo', 'Passe Errado']

  dicionario_pass_outcome = {
    stat: {Partida: sum((my_df.Nome_Pass_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas}
    for stat in stats_pass_outcome}

  print(dicionario_pass_outcome)

  # Definindo dicionário para stats da coluna nome_duelo
  stats_nome_duelo = ['Duelo no Chão', 'Duelo Aéreo']

  dicionario_nome_duelo = {
    stat: {Partida: sum((my_df.Nome_Duelo == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas} for stat
    in stats_nome_duelo}

  print(dicionario_nome_duelo)

  # Definindo dicionário para stats da coluna duelo_outcome
  stats_duelo_outcome = ['Duelo no Chão Ganho', 'Duelo Aéreo Ganho', 'Duelo no chão perdido', 'Duelo aéreo perdido']

  dicionario_duelo_outcome = {
    stat: {Partida: sum((my_df.Nome_Duelo_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas}
    for stat in stats_duelo_outcome}

  print(dicionario_duelo_outcome)

  # Definindo dicionário para stats da colune index_gol
  stat_index_gol = 1

  dicionario_index_gol = {
    'Gol': {Partida: sum((my_df.Index_Gol == stat_index_gol) & (my_df.Index_Partida == Partida)) for Partida in
            Partidas}}

  print(dicionario_index_gol)

  # Definindo dicionário para stats da coluna index_assistencia
  stat_index_assist = 1

  dicionario_index_assist = {
    'Assistência': {Partida: sum((my_df.Index_Assist == stat_index_assist) & (my_df.Index_Partida == Partida)) for
                    Partida in Partidas}}

  print(dicionario_index_assist)

  # Definindo dicionário para stats da coluna index_toque
  stat_index_toque = 1

  dicionario_index_toque = {
    'Toque': {Partida: sum((my_df.Index_Toque == stat_index_toque) & (my_df.Index_Partida == Partida)) for Partida in
              Partidas}}

  print(dicionario_index_toque)

  # Definindo dicionário para stats da coluna index_passe_longo
  stat_index_passe_longo = 1

  dicionario_index_passe_longo = {
    'Passe Longo': {Partida: sum((my_df.Index_Passe_Longo == stat_index_passe_longo) & (my_df.Index_Partida == Partida))
                    for Partida in Partidas}}

  print(dicionario_index_passe_longo)

  # Definindo dicionário para % de passes certos
  lista_passes = np.array(list(dicionario_nome_ato['Passe'].values()))
  lista_passes_certos = np.array(list(dicionario_pass_outcome['Passe Certo'].values()))

  print(lista_passes)
  print(lista_passes_certos)

  lista_percentual_passe_certo = lista_passes_certos / lista_passes

  dicionario_percent_passes_certo = {
    '% Passes certos': {Partida: lista_percentual_passe_certo[Partida - 1] for Partida in Partidas}}
  print(dicionario_percent_passes_certo)

  # Definindo dicionário para % de duelos aéreos ganhos
  lista_duelos_aereos = np.array(list(dicionario_nome_duelo['Duelo Aéreo'].values()))
  lista_duelos_aereos_vencidos = np.array(list(dicionario_duelo_outcome['Duelo Aéreo Ganho'].values()))

  print(lista_duelos_aereos)
  print(lista_duelos_aereos_vencidos)

  lista_percentual_duelos_aereos_vencidos = lista_duelos_aereos_vencidos / lista_duelos_aereos

  dicionario_percent_duelos_aereos_vencidos = {
    '% Duelos aéreos vencidos': {Partida: lista_percentual_duelos_aereos_vencidos[Partida - 1] for Partida in Partidas}}
  print(dicionario_percent_duelos_aereos_vencidos)

  # Definindo dicionário para % de duelos no chão ganhos
  lista_duelos_no_chao = np.array(list(dicionario_nome_duelo['Duelo no Chão'].values()))
  lista_duelos_no_chao_vencidos = np.array(list(dicionario_duelo_outcome['Duelo no Chão Ganho'].values()))

  print(lista_duelos_no_chao)
  print(lista_duelos_no_chao_vencidos)

  lista_percentual_duelos_no_chao_vencidos = lista_duelos_no_chao_vencidos / lista_duelos_no_chao

  dicionario_percent_duelos_no_chao_vencidos = {
    '% Duelos no chão vencidos': {Partida: lista_percentual_duelos_no_chao_vencidos[Partida - 1] for Partida in
                                  Partidas}}
  print(dicionario_percent_duelos_no_chao_vencidos)

  # Juntando os diversos dicionários em um único para o gráfico de evolução
  Dicionario_evolucao = {**dicionario_duelo_outcome, **dicionario_finalizacao_outcome, **dicionario_index_assist,
                         **dicionario_index_gol, **dicionario_index_passe_longo, **dicionario_index_toque,
                         **dicionario_nome_ato, **dicionario_nome_duelo, **dicionario_pass_outcome,
                         **dicionario_percent_duelos_aereos_vencidos, **dicionario_percent_duelos_no_chao_vencidos,
                         **dicionario_percent_passes_certo}
  print(Dicionario_evolucao)

  # Criando dicionario com nome do time visitante em cada partida
  dicionario_partidas_visitantes = {}
  for id_partida in Partidas:
    adversario = data.loc[data['Index_Partida'] == id_partida, 'Nome_Time_Visitante']
    pd_adversario = pd.DataFrame(adversario)
    data_partida = data.loc[data['Index_Partida'] == id_partida, 'Data']
    pd_data_partida = pd.DataFrame(data_partida)
    adversario = pd_adversario.Nome_Time_Visitante.unique()
    adversario = adversario.tolist()[0]
    data_partida = pd_data_partida.Data.unique()
    data_partida = data_partida.tolist()[0]
    dicionario_partidas_visitantes[id_partida] = adversario + ' - ' + data_partida
  print(dicionario_partidas_visitantes)

  # Criando dicionario evolucao com nome do time visitante
  dicionario_partidas_visitantes = {}
  for id_partida in Partidas:
    adversario = data.loc[data['Index_Partida'] == id_partida, 'Nome_Time_Visitante']
    pd_adversario = pd.DataFrame(adversario)
    data_partida = data.loc[data['Index_Partida'] == id_partida, 'Data']
    pd_data_partida = pd.DataFrame(data_partida)
    adversario = pd_adversario.Nome_Time_Visitante.unique()
    adversario = adversario.tolist()[0]
    data_partida = pd_data_partida.Data.unique()
    data_partida = data_partida.tolist()[0]
    dicionario_partidas_visitantes[id_partida] = adversario + ' - ' + data_partida
  print(dicionario_partidas_visitantes)

  # modificando o dicionario para nome de adversario

  stats = list(Dicionario_evolucao.keys())
  #stats = ['Gol', 'Assistência', 'Toque', 'Passe Certo','% Passes certos', 'Finalização', 'Finalização no gol', 'Finalização para fora', 'Finalização bloqueada', 'Perdas de posse', 'Duelo no Chão', '% Duelos no chão vencidos', 'Duelo Aéreo', '% Duelos aéreos vencidos', 'Desarme', 'Corte', 'Bloqueio de chute', 'Falta cometida', 'Falta sofrida', 'Cartão Amarelo', 'Cartão Vermelho']

  dic_partida_j = {}
  dic_stat = {}

  for stat in stats:
    for Partida in Partidas:
      dic_partida_i = {dicionario_partidas_visitantes[Partida]: Dicionario_evolucao[stat][Partida]}
      dic_partida_j = {**dic_partida_j, **dic_partida_i}
    dic_stat_j = {stat: dic_partida_j}
    dic_stat = {**dic_stat, **dic_stat_j}

  # Criando tabela geral

  lista_estatisticas = list(dic_stat.keys())
  Scouts = list(dic_stat.values())
  Partidas = list(dic_stat['Passe'].keys())
  adversario = list(
    dicionario_partidas_visitantes.values())  ## quando coloco essa variavel dentro do dataframe ele passa a nao entender os valores porque acho que estao em dicionarios diferentes
  df_data = pd.DataFrame(Scouts, columns=Partidas, index=lista_estatisticas)
  df_data = df_data.loc[(df_data.index != 'Duelo no Chão Ganho') & (df_data.index != 'Duelo Aéreo Ganho') & (df_data.index != 'Duelo no chão perdido') & (df_data.index != 'Duelo aéreo perdido') & (df_data.index != 'Passe Longo') & (df_data.index != 'Drible') & (df_data.index != 'Passe Certo') & (df_data.index != 'Passe Errado')]
  sorting = {'estatística': ['Gol', 'Assistência', 'Toque', 'Passe', '% Passes certos', 'Finalização', 'Finalização no gol', 'Finalização para fora', 'Finalização bloqueada', 'Perda de posse', 'Duelo no Chão', '% Duelos no chão vencidos', 'Duelo Aéreo', '% Duelos aéreos vencidos', 'Desarme', 'Corte', 'Bloqueio de chute', 'Falta cometida', 'Falta sofrida', 'Cartão Amarelo', 'Cartão Vermelho']}
  df_mapping = pd.DataFrame(sorting)
  sort_mapping  = df_mapping.reset_index().set_index('estatística')
  df_data['ordem'] = df_data.index.map(sort_mapping['index'])
  df_data = df_data.sort_values('ordem')
  df_data = df_data.drop(columns = ['ordem'])
  st.dataframe(df_data)

with tab3:
  
  tab5, tab6 = st.tabs(['Heat Map','Event Map'])
  
  # Desenhando o mapa de passes
  with tab6:
    
  # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

  # Pitch Outline & Centre Line
    ax.plot([0, 0], [0, 25], color="black")
    ax.plot([0, 45], [25, 25], color="black")
    ax.plot([45, 45], [25, 0], color="black")
    ax.plot([45, 0], [0, 0], color="black")
    ax.plot([22.5, 22.5], [0, 25], color="black")

  # Pitch shoot-out lines
    ax.plot([17.5, 17.5], [15, 10], color="black")
    ax.plot([27.5, 27.5], [15, 10], color="black")

  # Left Penalty Area
    ax.plot([8, 8], [20, 5], color="black")
    ax.plot([0, 8], [20, 20], color="black")
    ax.plot([8, 0], [5, 5], color="black")

  # Right Penalty Area
    ax.plot([45, 37], [20, 20], color="black")
    ax.plot([37, 37], [20, 5], color="black")
    ax.plot([37, 45], [5, 5], color="black")

  # Prepare Circles
    centreSpot = plt.Circle((22.5,12.5), 0.1, color="black")

  # Draw Circles
    ax.add_patch(centreSpot)

  # Tidy Axes
    ax.axis('off')

  # Criando caixa com estatísticas que podem ser selecionadas para os mapas
    lista_stats_mapa = ['Passes', 'Finalizacoes', 'Duelos', 'Desarmes', 'Perdas de Posse', 'Faltas Sofridas',
                        'Faltas Cometidas']
    option_stat_mapa = st.selectbox('Selecione uma estatística', lista_stats_mapa)

  # Desenhando eventos de opção selecionada

    for i in range(len(my_df)):

        if option_stat_mapa == 'Passes':
            if my_df['Nome_Pass_Outcome'][i] == 'Passe Certo':
                ax.plot([int(my_df["x_start"][i]), int(my_df["x_end"][i])],[int(my_df["y_start"][i]), int(my_df["y_end"][i])], color="blue")
                ax.plot(int(my_df["x_end"][i]), int(my_df["y_end"][i]), "o", color="blue")
            if my_df['Nome_Pass_Outcome'][i] == 'Passe Errado':
                ax.plot([int(my_df["x_start"][i]), int(my_df["x_end"][i])],[int(my_df["y_start"][i]), int(my_df["y_end"][i])], color="red")
                ax.plot(int(my_df["x_end"][i]), int(my_df["y_end"][i]), "o", color="red")

        if option_stat_mapa == 'Finalizacoes':
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização bloqueada':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="orange")
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização no gol':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="blue")
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização para fora':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="red")

        if option_stat_mapa == 'Faltas Cometidas':
            if my_df['Nome_Ato'][i] == 'Falta cometida':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="red")

        if option_stat_mapa == 'Faltas Sofridas':
            if my_df['Nome_Ato'][i] == 'Falta sofrida':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="blue")

        if option_stat_mapa == 'Perdas de Posse':
            if my_df['Nome_Ato'][i] == 'Perda de posse':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="red")

        if option_stat_mapa == 'Desarmes':
            if my_df['Nome_Ato'][i] == 'Desarme':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="blue")

        if option_stat_mapa == 'Duelos':
            if my_df['Nome_Duelo_Outcome'][i] == 'Duelo no Chão Ganho':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="blue")
            if my_df['Nome_Duelo_Outcome'][i] == 'Duelo no chão perdido':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="red")
            if my_df['Nome_Duelo_Outcome'][i] == 'Duelo Aéreo Ganho':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="blue")
            if my_df['Nome_Duelo_Outcome'][i] == 'Duelo aéreo perdido':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "x", color="red")
                
    st.pyplot(fig)
    
    # aba de heatmap
    
    with tab5:
        
        # Create figure
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

  # Pitch Outline & Centre Line
        ax.plot([0, 0], [0, 25], color="black")
        ax.plot([0, 45], [25, 25], color="black")
        ax.plot([45, 45], [25, 0], color="black")
        ax.plot([45, 0], [0, 0], color="black")
        ax.plot([22.5, 22.5], [0, 25], color="black")

  # Pitch shoot-out lines
        ax.plot([17.5, 17.5], [15, 10], color="black")
        ax.plot([27.5, 27.5], [15, 10], color="black")

  # Left Penalty Area
        ax.plot([8, 8], [20, 5], color="black")
        ax.plot([0, 8], [20, 20], color="black")
        ax.plot([8, 0], [5, 5], color="black")

  # Right Penalty Area
        ax.plot([45, 37], [20, 20], color="black")
        ax.plot([37, 37], [20, 5], color="black")
        ax.plot([37, 45], [5, 5], color="black")

  # Prepare Circles
        centreSpot = plt.Circle((22.5,12.5), 0.1, color="black")

  # Draw Circles
        ax.add_patch(centreSpot)

  # Tidy Axes
        ax.axis('off')
  
   # mapa de calor de toques
        customcmap = mat.colors.LinearSegmentedColormap.from_list('custom cmap', ['white', 'green'])

        toques_xstart = list(my_df.loc[my_df['Nome_Toque'] == "Sim", 'x_start'])
        toques_ystart = list(my_df.loc[my_df['Nome_Toque'] == "Sim", 'y_start'])
        sns.kdeplot(x=toques_xstart, y=toques_ystart, shade=True, shade_lowest=False, alpha=1, n_levels=200,
                  cmap=customcmap)

        plt.ylim(0, 25)
        plt.xlim(0, 45)

        st.pyplot(fig)

with tab2:
  # Criar lista com lista única das partidas
  Partidas = my_df.Index_Partida.unique()
  Partidas = Partidas.tolist()
  Partidas.sort()

  # Definindo dicionário para stats da coluna nome_ato
  stats_nome_ato = ['Passe', 'Finalização', 'Corte', 'Cartão Amarelo', 'Cartão Vermelho', 'Bloqueio de chute',
                    'Desarme',
                    'Drible', 'Falta cometida', 'Falta sofrida', 'Perda de posse']

  dicionario_nome_ato = {
    stat: {Partida: sum((my_df.Nome_Ato == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas} for stat
    in stats_nome_ato}

  print(dicionario_nome_ato)

  # Definindo dicionário para stats da coluna finalizacao_outcome
  stats_finalizacao_outcome = ['Finalização no gol', 'Finalização para fora', 'Finalização bloqueada']

  dicionario_finalizacao_outcome = {
    stat: {Partida: sum((my_df.Nome_Finalizacao_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in
           Partidas} for stat in stats_finalizacao_outcome}

  print(dicionario_finalizacao_outcome)

  # Definindo dicionário para stats da coluna pass_outcome
  stats_pass_outcome = ['Passe Certo', 'Passe Errado']

  dicionario_pass_outcome = {
    stat: {Partida: sum((my_df.Nome_Pass_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas}
    for stat in stats_pass_outcome}

  print(dicionario_pass_outcome)

  # Definindo dicionário para stats da coluna nome_duelo
  stats_nome_duelo = ['Duelo no Chão', 'Duelo Aéreo']

  dicionario_nome_duelo = {
    stat: {Partida: sum((my_df.Nome_Duelo == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas} for stat
    in stats_nome_duelo}

  print(dicionario_nome_duelo)

  # Definindo dicionário para stats da coluna duelo_outcome
  stats_duelo_outcome = ['Duelo no Chão Ganho', 'Duelo Aéreo Ganho', 'Duelo no chão perdido', 'Duelo aéreo perdido']

  dicionario_duelo_outcome = {
    stat: {Partida: sum((my_df.Nome_Duelo_Outcome == stat) & (my_df.Index_Partida == Partida)) for Partida in Partidas}
    for stat in stats_duelo_outcome}

  print(dicionario_duelo_outcome)

  # Definindo dicionário para stats da colune index_gol
  stat_index_gol = 1

  dicionario_index_gol = {
    'Gol': {Partida: sum((my_df.Index_Gol == stat_index_gol) & (my_df.Index_Partida == Partida)) for Partida in
            Partidas}}

  print(dicionario_index_gol)

  # Definindo dicionário para stats da coluna index_assistencia
  stat_index_assist = 1

  dicionario_index_assist = {
    'Assistência': {Partida: sum((my_df.Index_Assist == stat_index_assist) & (my_df.Index_Partida == Partida)) for
                    Partida in Partidas}}

  print(dicionario_index_assist)

  # Definindo dicionário para stats da coluna index_toque
  stat_index_toque = 1

  dicionario_index_toque = {
    'Toque': {Partida: sum((my_df.Index_Toque == stat_index_toque) & (my_df.Index_Partida == Partida)) for Partida in
              Partidas}}

  print(dicionario_index_toque)

  # Definindo dicionário para stats da coluna index_passe_longo
  stat_index_passe_longo = 1

  dicionario_index_passe_longo = {
    'Passe Longo': {Partida: sum((my_df.Index_Passe_Longo == stat_index_passe_longo) & (my_df.Index_Partida == Partida))
                    for Partida in Partidas}}

  print(dicionario_index_passe_longo)

  # Definindo dicionário para % de passes certos
  lista_passes = np.array(list(dicionario_nome_ato['Passe'].values()))
  lista_passes_certos = np.array(list(dicionario_pass_outcome['Passe Certo'].values()))

  print(lista_passes)
  print(lista_passes_certos)

  lista_percentual_passe_certo = lista_passes_certos / lista_passes

  dicionario_percent_passes_certo = {
    '% Passes certos': {Partida: lista_percentual_passe_certo[Partida - 1] for Partida in Partidas}}
  print(dicionario_percent_passes_certo)

  # Definindo dicionário para % de duelos aéreos ganhos
  lista_duelos_aereos = np.array(list(dicionario_nome_duelo['Duelo Aéreo'].values()))
  lista_duelos_aereos_vencidos = np.array(list(dicionario_duelo_outcome['Duelo Aéreo Ganho'].values()))

  print(lista_duelos_aereos)
  print(lista_duelos_aereos_vencidos)

  lista_percentual_duelos_aereos_vencidos = lista_duelos_aereos_vencidos / lista_duelos_aereos

  dicionario_percent_duelos_aereos_vencidos = {
    '% Duelos aéreos vencidos': {Partida: lista_percentual_duelos_aereos_vencidos[Partida - 1] for Partida in Partidas}}
  print(dicionario_percent_duelos_aereos_vencidos)

  # Definindo dicionário para % de duelos no chão ganhos
  lista_duelos_no_chao = np.array(list(dicionario_nome_duelo['Duelo no Chão'].values()))
  lista_duelos_no_chao_vencidos = np.array(list(dicionario_duelo_outcome['Duelo no Chão Ganho'].values()))

  print(lista_duelos_no_chao)
  print(lista_duelos_no_chao_vencidos)

  lista_percentual_duelos_no_chao_vencidos = lista_duelos_no_chao_vencidos / lista_duelos_no_chao

  dicionario_percent_duelos_no_chao_vencidos = {
    '% Duelos no chão vencidos': {Partida: lista_percentual_duelos_no_chao_vencidos[Partida - 1] for Partida in
                                  Partidas}}
  print(dicionario_percent_duelos_no_chao_vencidos)

  # Juntando os diversos dicionários em um único para o gráfico de evolução
  Dicionario_evolucao = {**dicionario_duelo_outcome, **dicionario_finalizacao_outcome, **dicionario_index_assist,
                         **dicionario_index_gol, **dicionario_index_passe_longo, **dicionario_index_toque,
                         **dicionario_nome_ato, **dicionario_nome_duelo, **dicionario_pass_outcome,
                         **dicionario_percent_duelos_aereos_vencidos, **dicionario_percent_duelos_no_chao_vencidos,
                         **dicionario_percent_passes_certo}
  print(Dicionario_evolucao)

  # Criando dicionario com nome do time visitante em cada partida
  dicionario_partidas_visitantes = {}
  for id_partida in Partidas:
    adversario = data.loc[data['Index_Partida'] == id_partida, 'Nome_Time_Visitante']
    pd_adversario = pd.DataFrame(adversario)
    data_partida = data.loc[data['Index_Partida'] == id_partida, 'Data']
    pd_data_partida = pd.DataFrame(data_partida)
    adversario = pd_adversario.Nome_Time_Visitante.unique()
    adversario = adversario.tolist()[0]
    data_partida = pd_data_partida.Data.unique()
    data_partida = data_partida.tolist()[0]
    dicionario_partidas_visitantes[id_partida] = adversario + ' - ' + data_partida
  print(dicionario_partidas_visitantes)

  # Criando dicionario evolucao com nome do time visitante
  dicionario_partidas_visitantes = {}
  for id_partida in Partidas:
    adversario = data.loc[data['Index_Partida'] == id_partida, 'Nome_Time_Visitante']
    pd_adversario = pd.DataFrame(adversario)
    data_partida = data.loc[data['Index_Partida'] == id_partida, 'Data']
    pd_data_partida = pd.DataFrame(data_partida)
    adversario = pd_adversario.Nome_Time_Visitante.unique()
    adversario = adversario.tolist()[0]
    data_partida = pd_data_partida.Data.unique()
    data_partida = data_partida.tolist()[0]
    dicionario_partidas_visitantes[id_partida] = adversario + ' - ' + data_partida
  print(dicionario_partidas_visitantes)

  # modificando o dicionario para nome de adversario

  stats = list(Dicionario_evolucao.keys())

  dic_partida_j = {}
  dic_stat = {}

  for stat in stats:
    for Partida in Partidas:
      dic_partida_i = {dicionario_partidas_visitantes[Partida]: Dicionario_evolucao[stat][Partida]}
      dic_partida_j = {**dic_partida_j, **dic_partida_i}
    dic_stat_j = {stat: dic_partida_j}
    dic_stat = {**dic_stat, **dic_stat_j}

  # Criando gráfico de evolução

  lista_estatisticas = list(dic_stat.keys())
  option = st.selectbox('Estatistica', lista_estatisticas)

  Stat = option
  Scouts = list(dic_stat[Stat].values())
  Partidas = list(dic_stat[Stat].keys())
  chart_data = pd.DataFrame(Scouts, Partidas)

  st.bar_chart(chart_data)
  
  st.dataframe(chart_data)
  st.write(chart_data[0])
  st.write(chart_data.index)  
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  ax = chart_data.plot.bar(x=chart_data.index, y=0, rot=0)
  st.pyplot(fig)
    
with tab4:
  # Puxando o arquivo com a base de videos
  sheet_id = '15Zkt-YrhKGC3JKdPhGl5tjQhaeCfihJiGUev1DKP52o'
  sheet_name = 'Videos'
  url = 'https://docs.google.com/spreadsheets/d/'+sheet_id+'/gviz/tq?tqx=out:csv&sheet='+sheet_name
  data_videos = pd.read_csv(url)
    
  # Convertendo base de videos para dataframe

  my_df_video = pd.DataFrame(data_videos)

  # Criar lista com lista única das partidas
  Partidas = my_df.Index_Partida.unique()
  Partidas = Partidas.tolist()
  Partidas.sort()

  # Criando dicionario com nome do time visitante em cada partida
  dicionario_partidas_visitantes = {}
  for id_partida in Partidas:
    adversario = data.loc[data['Index_Partida'] == id_partida, 'Nome_Time_Visitante']
    pd_adversario = pd.DataFrame(adversario)
    data_partida = data.loc[data['Index_Partida'] == id_partida, 'Data']
    pd_data_partida = pd.DataFrame(data_partida)
    adversario = pd_adversario.Nome_Time_Visitante.unique()
    adversario = adversario.tolist()[0]
    data_partida = pd_data_partida.Data.unique()
    data_partida = data_partida.tolist()[0]
    dicionario_partidas_visitantes[id_partida] = adversario + ' - ' + data_partida

  # Convertendo dicionario de partidas visitantes em dataframe
  df_visitantes = pd.DataFrame(dicionario_partidas_visitantes.items(), columns=['id_partida', 'nome_visitante'])

  # Definindo filtros para stats e partidas
  filtros_stats_videos = ['Gols', 'Assistências', 'Passes', 'Finalizações', 'Duelos', 'Desarmes', 'Perdas de posse',
                          'Toques']
  filtros_partidas_videos = list(dicionario_partidas_visitantes.values())
  option_stat_video = st.multiselect('Selecione as estatísticas', filtros_stats_videos)
  option_partidas_videos = st.multiselect('Selecione as partidas', filtros_partidas_videos)

  # Condicional para ver se filtros foram selecionados
  if option_partidas_videos == [] or option_stat_video ==[]:
    st.write('Para visualizar os videos é necessário selecionar pelo menos uma estatística E uma partida')
  else:
  
    
    
    
  # Puxando o id_partida das partidas selecionadas
    partidas_selecionadas_videos = pd.DataFrame()

    for partida_selecionada in option_partidas_videos:
        partida_selecionada_videos_i = pd.DataFrame(
            df_visitantes.loc[df_visitantes['nome_visitante'] == partida_selecionada])
        partidas_selecionadas_videos = partidas_selecionadas_videos.append(partida_selecionada_videos_i, ignore_index=True)

  # criando lista única de ids de partidas selecionadas
    lista_id_partidas_selecionadas = partidas_selecionadas_videos.id_partida.unique()
    lista_id_partidas_selecionadas = lista_id_partidas_selecionadas.tolist()

  # puxando o id dos videos de partidas e estatisticas selecionadas

    df_videos_selecionados = pd.DataFrame()

    for partida_selecionada in lista_id_partidas_selecionadas:
        for stat_selecionada in option_stat_video:
            df_videos_selecionados_i = pd.DataFrame(my_df_video.loc[(my_df_video['Index_Partida'] == partida_selecionada) & (
                my_df_video['Nome_Stat_Video'] == stat_selecionada)])
        df_videos_selecionados = df_videos_selecionados.append(df_videos_selecionados_i)

  # puxando lista com index dos videos selecionados
    lista_id_videos_selecionados = df_videos_selecionados.Index_Video.unique()
    lista_id_videos_selecionados = lista_id_videos_selecionados.tolist()

  

  # puxando videos selecionados e fazendo upload online
    for video in lista_id_videos_selecionados:
        url = data_videos.loc[video-1,'Link_youtube']
        estatistica = data_videos.loc[video-1,'Nome_Stat_Video']
        legenda = estatistica+':'
    # Create a VideoCapture object
        st.write(legenda)
        st.video(url)

