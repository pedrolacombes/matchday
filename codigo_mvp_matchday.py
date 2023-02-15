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

tab1, tab2, tab3, tab6= st.tabs(['Tabela Geral','Mapas','Videos', 'Ranking'])

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

with tab2:
  
  tab4, tab5 = st.tabs(['Event Map','Heat Map'])
  
  # Desenhando o mapa de passes
  with tab4:
    
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
    
  # Draw sentido do campo
    sentido = plt.arrow(18, 26, 8, 0, color="black", head_width = 0.4)
    ax.add_patch(sentido)

  # Draw Circles
    ax.add_patch(centreSpot)

  # Tidy Axes
    ax.axis('off')

  # Criando caixa com estatísticas que podem ser selecionadas para os mapas
    lista_stats_mapa = ['Passes', 'Finalizacoes', 'Duelos', 'Desarmes', 'Perdas de Posse', 'Faltas Sofridas',
                        'Faltas Cometidas']
    option_stat_mapa = st.selectbox('Selecione uma estatística', lista_stats_mapa)

  # Desenhando eventos de opção selecionada

    if option_stat_mapa == 'Passes':
            distancia = st.slider('Passes que ganharam pelo menos x metros de campo (selecionar -45 irá mostrar todos os passes)', -45, 45, 1)

    contagem_passe_certo = 0
    contagem_passe_errado = 0
    
    for i in range(len(my_df)):
        
        if option_stat_mapa == 'Passes':
            if my_df['Nome_Pass_Outcome'][i] == 'Passe Certo' and ((my_df['x_end'][i]-my_df['x_start'][i])>distancia):
                ax.plot([int(my_df["x_start"][i]), int(my_df["x_end"][i])],[int(my_df["y_start"][i]), int(my_df["y_end"][i])], color="blue", linewidth =0.6)
                ax.plot(int(my_df["x_end"][i]), int(my_df["y_end"][i]), "o", color="blue", markersize=2)
                contagem_passe_certo += 1
            if my_df['Nome_Pass_Outcome'][i] == 'Passe Errado' and ((my_df['x_end'][i]-my_df['x_start'][i])>distancia):
                ax.plot([int(my_df["x_start"][i]), int(my_df["x_end"][i])],[int(my_df["y_start"][i]), int(my_df["y_end"][i])], color="red", linewidth =0.6)
                ax.plot(int(my_df["x_end"][i]), int(my_df["y_end"][i]), "o", color="red", markersize=2)
                contagem_passe_errado += 1
            ax.plot(0,26,'o',color='blue')
            ax.plot(0,27,'o',color='red')
            ax.text(1,25.75,'Passes certos',fontsize=6)
            ax.text(1,26.75,'Passes errados', fontsize=6)
            
        if option_stat_mapa == 'Finalizacoes':
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização bloqueada':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="orange")
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização no gol':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="blue")
            if my_df['Nome_Finalizacao_Outcome'][i] == 'Finalização para fora':
                plt.plot(int(my_df["x_start"][i]), int(my_df["y_start"][i]), "o", color="red")
            ax.plot(0,26,'o',color='orange')
            ax.plot(0,27,'o',color='blue')
            ax.plot(0,28,'o',color='red')
            ax.text(1,25.75,'Finalização bloqueada',fontsize=6)
            ax.text(1,26.75,'Finalização no gol', fontsize=6)
            ax.text(1,27.75,'Finalização para fora', fontsize=6)

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
            ax.plot(0,26,'o',color='blue')
            ax.plot(0,27,'o',color='red')
            ax.plot(0,28,'x',color='blue')
            ax.plot(0,29,'x',color='red')
            ax.text(1,25.75,'Duelo no chão ganho',fontsize=6)
            ax.text(1,26.75,'Duelo no chão perdido', fontsize=6)
            ax.text(1,27.75,'Duelo aéreo ganho', fontsize=6)
            ax.text(1,28.75,'Duelo aéreo perdido', fontsize=6)
                
    st.pyplot(fig)
    
    if option_stat_mapa == 'Passes':
        st.write(f"Ao todo foram {contagem_passe_certo + contagem_passe_errado} passes com ganho de mais de {distancia} metros de campo")
        st.write(f"Desse total, {contagem_passe_certo / (contagem_passe_certo + contagem_passe_errado):.0%} foram passes certos")
    
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
    
  # Draw sentido do campo
        sentido = plt.arrow(18, 12.5, 8, 0, color="black", head_width = 0.4)
        ax.add_patch(sentido)


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

with tab3:
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
        visitante_data = data_videos.loc[video-1,'Visitante_Data']
    # Create a VideoCapture object
        if url == 'Null':
            st.write(f'Não há vídeos de {estatistica} para a partida vs. {visitante_data}')
        else:
            legenda = estatistica+' vs. '+visitante_data+':'
            st.write(legenda)
            st.video(url)


	
with tab6:
	
	tab7, tab8 = st.tabs(['Melhores Jogadores', 'Compare'])
	
	with tab7:
		
		# Colocando os filtros na tela
		
		stats_ranking = ['Classificação média Matchday', 'Gol + Assistência', 'Gol', 'Assistência', 'Finalização', 'Finalização no gol', 'Toque', 'Passe certo', '% Passe certo', 'Drible bem sucedido', 'Perda de posse', 'Duelo no chão ganho', 'Duelo aéreo ganho', 'Desarme', 'Corte', 'Bloqueio de chute', 'Falta sofrida', 'Falta cometida', 'Cartão Amarelo', 'Cartão Vermelho']
		Estatistica = st.selectbox('Selecione uma estatística:',stats_ranking)
		tipos_ordem = ['Total', 'Por jogo']
		Ordem = st.selectbox('Ordenar por:', tipos_ordem)
		
		if Ordem == 'Total':
			Ordem = 'Total_Estatistica_Ranking'
		else:
			Ordem = 'Media_Estatistica_Ranking'

		# Puxando o arquivo com a base ranking

		sheet_id = '15Zkt-YrhKGC3JKdPhGl5tjQhaeCfihJiGUev1DKP52o'
		sheet_name = 'Ranking'
		url = 'https://docs.google.com/spreadsheets/d/'+sheet_id+'/gviz/tq?tqx=out:csv&sheet='+sheet_name
		data = pd.read_csv(url)
		data.head()
		
		# Alterando dataframe para estatística selecionada
		data = data[data['Nome_Estatistica_Ranking'] == Estatistica]
		data.sort_values(by=[Ordem], ascending=True, inplace=True)
		data.reset_index(inplace = True)
		data.drop(['index'],inplace=True, axis=1)
		
		# Criando figura

		fig, ax = plt.subplots(figsize=(7,6))

		# Definindo número de linhas e colunas

		cols = 4
		rows = 10

		# Criar coordenadas com base no número de linhas e colunas

		# Adicionando bordas

		ax.set_ylim(-1, rows + 1)
		ax.set_xlim(0.25, cols-0.5)

		# from the sample data, each dict in the list represents one row

		# each key in the dict represents a column

		for row in range(rows):
			# extract the row data from the list

		    d = data.loc[row]

		    # the y (row) coordinate is based on the row index (loop)

		    # the x (column) coordinate is defined based on the order I want to display the data in


		    # posicao column

		    ax.text(x=.5, y=row, s=10-row, va='center', ha='right')

		    # nome jogador column

		    ax.text(x=1.5, y=row, s=d['Nome_Jogador'], va='center', ha='right')

		    # total column

		    ax.text(x=2.5, y=row, s=d['Total_Estatistica_Ranking'], va='center', ha='right')

		    # media column

		    ax.text(x=3.5, y=row, s=d['Media_Estatistica_Ranking'], va='center', ha='right')


		    # Add column headers

		# plot them at height y=9.75 to decrease the space to the

		# first data row (you'll see why later)

		ax.text(0.5, 9.75, 'Posição', weight='bold', ha='center')
		ax.text(1.5, 9.75, 'Player', weight='bold', ha='right')
		ax.text(2.5, 9.75, 'Total', weight='bold', ha='right')
		ax.text(3.5, 9.75, 'Média / Jogo', weight='bold', ha='right')

		for row in range(rows):
		    ax.plot(
			[0.25, cols-0.5],
			[row -.5, row - .5],
			ls=':',
			lw='.5',
			c='grey'
		    )

		# add a main header divider

		# remember that we plotted the header row slightly closer to the first data row

		# this helps to visually separate the header row from the data rows

		# each data row is 1 unit in height, thus bringing the header closer to our 

		# gridline gives it a distinctive difference.

		ax.plot([0.25, cols-0.5], [9.5, 9.5], lw='.5', c='black')

		ax.axis('off')
		
		fig
	
	with tab8:
		lista_jogadores = ['Samir', 'Lucas', 'Pedro', 'Fernando', 'Luiz', 'João', 'Felipe']
		Jogador1 = st.selectbox('Selecione o primeiro jogador:', lista_jogadores)
		Jogador2 = st.selectbox('Selecione o segundo jogador:', lista_jogadores)
		
		# Definindo a lista de estatísticas de comparação
		lista_stats_comp = ['Classificação média Matchday', 'Gol + Assistência', 'Gol', 'Assistência', 'Finalização', 'Finalização no gol', 'Toque', 'Passe certo', '% Passe certo', 'Drible bem sucedido', 'Perda de posse', 'Duelo no chão ganho', 'Duelo aéreo ganho', 'Corte', 'Desarme', 'Bloqueio de chute', 'Falta sofrida', 'Falta cometida', 'Cartão Amarelo', 'Cartão Vermelho']
		
		# Criando figura

		fig, ax = plt.subplots(figsize=(8,20))

		# Definindo número de linhas e colunas

		cols = 3
		rows = 20

		# Criar coordenadas com base no número de linhas e colunas

		# Adicionando bordas

		ax.set_ylim(-1, rows + 1)
		ax.set_xlim(0.25, cols-0.5)

		# setando a linha inicial

		linha = 20

		# loop para preencher a tabela chamando as estatísticas

		for stat_comp in lista_stats_comp:
		  stat_jogador1 = data_jogador1.loc[data['Nome_Estatistica_Ranking'] == stat_comp, 'Media_Estatistica_Ranking'].values[0]
		  stat_jogador2 = data_jogador2.loc[data['Nome_Estatistica_Ranking'] == stat_comp, 'Media_Estatistica_Ranking'].values[0]
		  ax.text(x=0.5, y=linha, s=stat_jogador1, va='center', ha='right')
		  ax.text(x=2.25, y=linha, s=stat_jogador2, va='center', ha='right')
		  ax.text(x=1.325, y=linha, s=stat_comp+' por jogo', va='center', ha='center')
		  linha = linha - 1

		# colocando cabeçalho
		ax.text(0.5, 20.75, Jogador1, weight='bold', ha='right')
		ax.text(1.325, 20.75, 'Stat', weight='bold', ha='center')
		ax.text(2.25, 20.75, Jogador2, weight='bold', ha='right')
		ax.plot([0.25, cols-0.62], [20.5, 20.5], lw='.5', c='black')

		# tirando eixos
		ax.axis('off')

		#plotando figura streamlit
		fig
