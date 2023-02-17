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

tab1, tab2, tab3, tab6= st.tabs(['Meu Perfil','Meus Mapas','Meus Videos', 'Ranking'])

# montando pagina do tabelao

with tab1:
	
	tab9, tab10, tab11 = st.tabs(['Resumo', 'Stats Overview', 'Partidas'])
	
	with tab9:
		# Criando figura
		fig, ax = plt.subplots(figsize=(10,20))

		# Definindo número de linhas e colunas

		cols = 40
		rows = 40

		# Criar coordenadas com base no número de linhas e colunas

		# Adicionando bordas

		ax.set_ylim(0, rows)
		ax.set_xlim(0, cols)

		# Traçando linhas divisórias
		ax.plot([1, 39], [36, 36], lw='.2', c='gray')
		ax.plot([1, 39], [28, 28], lw='.2', c='gray')
		ax.plot([1, 39], [14, 14], lw='.2', c='gray')


		# colocando o time em que joga
		ax.text(1,38, 'Samir Hauache', weight='bold', ha='left', va='center', fontsize = 28)
		ax.text(1,37, 'Time: Canela de Pedreiro', ha='left', va='center', fontsize = 18, color='grey')
		

		# colocando dados gerais
		ax.text(7.33, 34, 'Brasil', ha='center', va='center', fontsize = 16)
		ax.text(20, 34, '30 anos', ha='center', va='center', fontsize = 16)
		ax.text(32.66, 34, '177 cm', ha='center', va='center', fontsize = 16)
		ax.text(7.33, 31, 'Destro', ha='center', va='center', fontsize = 16)
		ax.text(20, 31, 'MEI', ha='center', va='center', fontsize = 16)
		ax.text(32.66, 31, '5', ha='center', va='center', fontsize = 16)
		ax.text(7.33, 33, 'Nacionalidade', ha='center', va='center', fontsize = 14, color='grey')
		ax.text(20, 33, 'Idade', ha='center', va='center', fontsize = 14, color='grey')
		ax.text(32.66, 33, 'Altura', ha='center', va='center', fontsize = 14, color = 'grey')
		ax.text(7.33, 30, 'Pé de preferência', ha='center', va='center', fontsize = 14, color='grey')
		ax.text(20, 30, 'Posição', ha='center', va='center', fontsize = 14,color='grey')
		ax.text(32.66, 30, '# Camisa', ha='center', va='center', fontsize = 14,color='grey')

		# plotando o pentagono de skills
		coord = [[20, 26], [9, 22],[13.2,15.54],[26.8,15.54],[31,22]]
		coord.append(coord[0])
		xs, ys = zip(*coord)

		ax.plot(xs,ys, color='grey', alpha=0.3)
		ax.fill(xs,ys, color='grey', alpha=0.1)

		ax.plot([20,20], [20.5,26], color='grey', alpha=0.3)
		ax.plot([20,9], [20.5,22], color='grey',alpha=0.3)
		ax.plot([20,13.2], [20.5,15.54], color='grey',alpha=0.3)
		ax.plot([20,26.8], [20.5,15.54], color='grey',alpha=0.3)
		ax.plot([20,31], [20.5,22], color='grey',alpha=0.3)
		
		att = 57
		cre = 63
		tec = 67
		tac = 65
		deff = 62
		x_cent = 20
		y_cent = 20.5
		x_att_full = 20
		y_att_full = 26
		x_cre_full = 9
		y_cre_full = 22
		x_tec_full = 31
		y_tec_full = 22
		x_tac_full = 26.8
		y_tac_full = 15.54
		x_deff_full = 13.2
		y_deff_full = 15.54
		x_att = x_cent + (x_att_full - x_cent) * (att / 100)
		y_att = y_cent + (y_att_full - y_cent) * (att / 100)
		x_cre = x_cent + (x_cre_full - x_cent) * (cre / 100)
		y_cre = y_cent + (y_cre_full - y_cent) * (cre / 100)
		x_tec = x_cent + (x_tec_full - x_cent) * (tec / 100)
		y_tec = y_cent + (y_tec_full - y_cent) * (tec / 100)
		x_tac = x_cent + (x_tac_full - x_cent) * (tac / 100)
		y_tac = y_cent + (y_tac_full - y_cent) * (tac / 100)
		x_deff = x_cent + (x_deff_full - x_cent) * (deff / 100)
		y_deff = y_cent + (y_deff_full - y_cent) * (deff / 100)

		coord_int = [[x_att,y_att],[x_cre,y_cre],[x_deff, y_deff],[x_tac,y_tac],[x_tec,y_tec]]
		coord_int.append(coord_int[0])
		xsi,ysi = zip(*coord_int)

		ax.plot(xsi,ysi, color='green', alpha=0.3)
		ax.fill(xsi,ysi, color='green', alpha=0.3)

		ax.text(1.25,27,s='Visão geral atributos', color='grey', fontsize = 12, ha='left')
		ax.text(20,26.5,s='ATT '+str(att), color='white', fontsize = 12, ha='center', bbox = dict(facecolor='green', alpha=0.45))
		ax.text(8.5,22,s='CRE '+str(cre), color='white', fontsize = 12, ha='right', bbox = dict(facecolor='green', alpha=0.45))
		ax.text(31.5,22,s='TEC '+str(cre), color='white', fontsize = 12, ha='left', bbox = dict(facecolor='green', alpha=0.45))
		ax.text(27.3,14.8,s='TAC '+str(cre), color='white', fontsize = 12, ha='left', bbox = dict(facecolor='green', alpha=0.45))
		ax.text(12.7,14.8,s='DEF '+str(deff), color='white', fontsize = 12, ha='right', bbox = dict(facecolor='green', alpha=0.45))
		
		# Desenhando grafico classificação
		ax.text(20, 13, s='Média mensal rating Matchday (últimos 12 meses)', color = 'grey', ha='center', fontsize=16)

		coord = [[0, 12], [40, 12],[40,0],[0,0]]
		coord.append(coord[0])
		xs, ys = zip(*coord)

		ax.plot(xs,ys, color='grey', alpha=0.0)
		ax.fill(xs,ys, color='grey', alpha=0.1)

		ax.bar(3.25,5.7,width=2.8,bottom=1,align='center', color = 'red', alpha = 0.9)
		ax.bar(6.25,6.3,width=2.8,bottom=1,align='center', color = 'orange', alpha = 0.9)
		ax.bar(9.25,6.8,width=2.8,bottom=1,align='center', color = 'orange', alpha = 0.9)
		ax.bar(12.25,8.2,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.7)
		ax.bar(15.25,7.4,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.4)
		ax.bar(18.25,7.2,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.4)
		ax.bar(21.25,6.5,width=2.8,bottom=1,align='center', color = 'orange', alpha = 0.9)
		ax.bar(24.25,8.4,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.7)
		ax.bar(27.25,7.7,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.4)
		ax.bar(30.25,7.5,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.4)
		ax.bar(33.25,5.9,width=2.8,bottom=1,align='center', color = 'red', alpha = 0.9)
		ax.bar(36.25,7.7,width=2.8,bottom=1,align='center', color = 'green', alpha = 0.4)

		ax.text(3.25,0.35,s='5.7', color='red', fontsize = 12, ha='center', alpha=0.9)
		ax.text(6.25,0.35,s='6.3', color='orange', fontsize = 12, ha='center', alpha=0.9)
		ax.text(9.25,0.35,s='6.8', color='orange', fontsize = 12, ha='center', alpha=0.9)
		ax.text(12.25,0.35,s='8.2', color='green', fontsize = 12, ha='center', alpha=0.7)
		ax.text(15.25,0.35,s='7.4', color='green', fontsize = 12, ha='center', alpha=0.4)
		ax.text(18.25,0.35,s='7.2', color='green', fontsize = 12, ha='center', alpha=0.4)
		ax.text(21.25,0.35,s='6.5', color='orange', fontsize = 12, ha='center', alpha=0.9)
		ax.text(24.25,0.35,s='8.4', color='green', fontsize = 12, ha='center', alpha=0.7)
		ax.text(27.25,0.35,s='7.7', color='green', fontsize = 12, ha='center', alpha=0.4)
		ax.text(30.25,0.35,s='7.5', color='green', fontsize = 12, ha='center', alpha=0.4)
		ax.text(33.25,0.35,s='5.9', color='red', fontsize = 12, ha='center', alpha=0.9)
		ax.text(36.25,0.35,s='7.7', color='green', fontsize = 12, ha='center', alpha=0.4)

		ax.text(3.25,11,s='Jan', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(6.25,11,s='Fev', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(9.25,11,s='Mar', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(12.25,11,s='Abr', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(15.25,11,s='Mai', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(18.25,11,s='Jun', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(21.25,11,s='Jul', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(24.25,11,s='Ago', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(27.25,11,s='Set', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(30.25,11,s='Out', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(33.25,11,s='Nov', color='grey', fontsize = 12, ha='center', alpha=0.9)
		ax.text(36.25,11,s='Dez', color='grey', fontsize = 12, ha='center', alpha=0.9)
		
		ax.axis('off')
		
		fig
		
	# Codigo para a pagina de estatistica por jogo
	
	with tab11:

	  # Alterando dataframe para pegar apenas linhas com informação
		bd_geral = my_df[my_df['Nome_Jogador'] == 'Samir']
		bd_geral.reset_index(inplace = True)

	  # Puxando a base de partidas
		sheet_id = '15Zkt-YrhKGC3JKdPhGl5tjQhaeCfihJiGUev1DKP52o'
		sheet_name = 'Partidas'
		url = 'https://docs.google.com/spreadsheets/d/'+sheet_id+'/gviz/tq?tqx=out:csv&sheet='+sheet_name
		bd_partidas = pd.read_csv(url)

	  # Definindo lista de partidas que podem ser selecionadas
		lista_partidas_selecionaveis = bd_partidas.Nome_Completo_Partida.unique()
		lista_partidas_selecionaveis = lista_partidas_selecionaveis.tolist()
		lista_selecao_partidas = st.selectbox('Selecione uma partida', lista_partidas_selecionaveis)


	  # Filtrando base geral para infos da partida selecionada
		partida_selecionada = lista_selecao_partidas
		id_partida_selecionada = bd_partidas.loc[bd_partidas['Nome_Completo_Partida'] == partida_selecionada, 'Index_Partida'].values[0]
		bd_partida_selecionada = bd_geral[bd_geral['Index_Partida']==id_partida_selecionada]
		bd_partida_selecionada.reset_index(inplace = True)

	  # Declarando as variáveis da tabela
	  # Definindo dicionário para stats da coluna nome_ato
		stats_nome_ato = ['Passe', 'Finalização', 'Corte', 'Cartão Amarelo', 'Cartão Vermelho', 'Bloqueio de chute','Desarme', 'Drible', 'Falta cometida', 'Falta sofrida', 'Perda de posse']

		dicionario_nome_ato = {stat: sum(bd_partida_selecionada.Nome_Ato == stat) for stat in stats_nome_ato}

	  # Definindo dicionário para stats da coluna finalizacao_outcome
		stats_finalizacao_outcome = ['Finalização no gol', 'Finalização para fora', 'Finalização bloqueada']

		dicionario_finalizacao_outcome = {stat: sum(bd_partida_selecionada.Nome_Finalizacao_Outcome == stat) for stat in stats_finalizacao_outcome}

	  # Definindo dicionário para stats da coluna pass_outcome
		stats_pass_outcome = ['Passe Certo', 'Passe Errado']

		dicionario_pass_outcome = {stat: sum(bd_partida_selecionada.Nome_Pass_Outcome == stat) for stat in stats_pass_outcome}

	  # Definindo dicionário para stats da coluna nome_duelo
		stats_nome_duelo = ['Duelo no Chão', 'Duelo Aéreo']

		dicionario_nome_duelo = {stat: sum(bd_partida_selecionada.Nome_Duelo == stat) for stat in stats_nome_duelo}

	  # Definindo dicionário para stats da coluna duelo_outcome
		stats_duelo_outcome = ['Duelo no Chão Ganho', 'Duelo Aéreo Ganho', 'Duelo no chão perdido', 'Duelo aéreo perdido']

		dicionario_duelo_outcome = {stat: sum(bd_partida_selecionada.Nome_Duelo_Outcome == stat) for stat in stats_duelo_outcome}

	  # Definindo dicionário para stats da colune index_gol
		stat_index_gol = 1

		dicionario_index_gol = {'Gol': sum(bd_partida_selecionada.Index_Gol == stat_index_gol)}

	  # Definindo dicionário para stats da coluna index_assistencia
		stat_index_assist = 1

		dicionario_index_assist = {'Assistência': sum(bd_partida_selecionada.Index_Assist == stat_index_assist)}

	  # Definindo dicionário para stats da coluna index_toque
		stat_index_toque = 1

		dicionario_index_toque = {'Toque': sum(bd_partida_selecionada.Index_Toque == stat_index_toque)}

	  # Definindo dicionário para stats da coluna index_passe_longo
		stat_index_passe_longo = 1

		dicionario_index_passe_longo = {'Passe Longo': sum(bd_partida_selecionada.Index_Passe_Longo == stat_index_passe_longo)}

	  # Definindo dicionário para % de passes certos
		lista_percentual_passe_certo = dicionario_pass_outcome['Passe Certo'] / dicionario_nome_ato['Passe']
		lista_percentual_passe_certo = '{:.1%}'.format(lista_percentual_passe_certo)

		dicionario_percent_passes_certo = {'% Passes certos': lista_percentual_passe_certo}

	  # Definindo dicionário para % de duelos aéreos ganhos
		lista_percentual_duelos_aereos_vencidos = dicionario_duelo_outcome['Duelo Aéreo Ganho'] / dicionario_nome_duelo['Duelo Aéreo']
		lista_percentual_duelos_aereos_vencidos = '{:.1%}'.format(lista_percentual_duelos_aereos_vencidos)

		dicionario_percent_duelos_aereos_vencidos = {'% Duelos aéreos vencidos': lista_percentual_duelos_aereos_vencidos}

	  # Definindo dicionário para % de duelos no chão ganhos
		lista_percentual_duelos_no_chao_vencidos = dicionario_duelo_outcome['Duelo no Chão Ganho'] / dicionario_nome_duelo['Duelo no Chão']
		lista_percentual_duelos_no_chao_vencidos = '{:.1%}'.format(lista_percentual_duelos_no_chao_vencidos)

		dicionario_percent_duelos_no_chao_vencidos = {'% Duelos no chão vencidos': lista_percentual_duelos_no_chao_vencidos}

	  # Definindo dicionário gols + assistências
		gols_assistencias = dicionario_index_gol['Gol'] + dicionario_index_assist['Assistência']

		dicionario_gol_assist = {'Gols + Assistências': gols_assistencias}

	  # Definindo dicionário classificação média matchday
		dicionario_clas_matchday = {'Classificação média Matchday': 7.9}

	  # Juntando os diversos dicionários em um único para o gráfico de evolução
		Dicionario_evolucao = {**dicionario_duelo_outcome, **dicionario_finalizacao_outcome, **dicionario_index_assist,
				       **dicionario_index_gol, **dicionario_index_passe_longo, **dicionario_index_toque,
				       **dicionario_nome_ato, **dicionario_nome_duelo, **dicionario_pass_outcome,
				       **dicionario_percent_duelos_aereos_vencidos, **dicionario_percent_duelos_no_chao_vencidos,
				       **dicionario_percent_passes_certo, **dicionario_gol_assist, **dicionario_clas_matchday}

	  # Plotando as informações da partida em uma tabela

	  #Definindo lista de estatisticas em ordem
		stats = ['Classificação média Matchday', 'Gols + Assistências', 'Gol', 'Assistência', 'Finalização', 'Finalização no gol', 'Finalização para fora', 'Finalização bloqueada', 'Toque', 'Passe Certo', '% Passes certos', 
			 'Perda de posse', 'Duelo no Chão Ganho', '% Duelos no chão vencidos', 'Duelo Aéreo Ganho','% Duelos aéreos vencidos', 'Desarme', 'Corte', 'Bloqueio de chute', 'Falta sofrida', 'Falta cometida', 
			 'Cartão Amarelo', 'Cartão Vermelho']

	  # Criando figura

		fig, ax = plt.subplots(figsize=(8,24))

	  # Definindo número de linhas e colunas

		cols = 3
		rows = 24

	  # Criar coordenadas com base no número de linhas e colunas

	  # Adicionando bordas

		ax.set_ylim(-1, rows + 1)
		ax.set_xlim(0.25, cols-0.5)

	  # setando a linha inicial

		linha = 24

	  # loop para preencher a tabela chamando as estatísticas

		for stat in stats:
			stat_valor = Dicionario_evolucao[stat]
			ax.text(x=0.25, y=linha, s=stat, va='center', ha='left')
			ax.text(x=2.25, y=linha, s=stat_valor, ha='right')
			linha = linha - 1

	  # colocando cabeçalho
		ax.text(0.25, 24.75, 'Stat', weight='bold', ha='left')
		ax.text(2.25, 24.75, 'Valor', weight='bold', ha='right')
		ax.plot([0.25, cols-0.62], [24.5, 24.5], lw='.5', c='black')

		ax.plot([0.25, cols-0.62], [23.5, 23.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [16.5, 16.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [12.5, 12.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [5.5, 5.5], lw='.2', c='gray')

	  # tirando eixos
		ax.axis('off')

		fig
	
	# Criando aba por campeonato
	
	with tab10:
		
		# Declarando as variáveis da tabela
		# Definindo dicionário para stats da coluna nome_ato
		stats_nome_ato = ['Passe', 'Finalização', 'Corte', 'Cartão Amarelo', 'Cartão Vermelho', 'Bloqueio de chute','Desarme', 'Drible', 'Falta cometida', 'Falta sofrida', 'Perda de posse']

		dicionario_nome_ato = {stat: sum(my_df.Nome_Ato == stat) for stat in stats_nome_ato}

		# Definindo dicionário para stats da coluna finalizacao_outcome
		stats_finalizacao_outcome = ['Finalização no gol', 'Finalização para fora', 'Finalização bloqueada']

		dicionario_finalizacao_outcome = {stat: sum(my_df.Nome_Finalizacao_Outcome == stat) for stat in stats_finalizacao_outcome}

		# Definindo dicionário para stats da coluna pass_outcome
		stats_pass_outcome = ['Passe Certo', 'Passe Errado']

		dicionario_pass_outcome = {stat: sum(my_df.Nome_Pass_Outcome == stat) for stat in stats_pass_outcome}

		# Definindo dicionário para stats da coluna nome_duelo
		stats_nome_duelo = ['Duelo no Chão', 'Duelo Aéreo']

		dicionario_nome_duelo = {stat: sum(my_df.Nome_Duelo == stat) for stat in stats_nome_duelo}

		# Definindo dicionário para stats da coluna duelo_outcome
		stats_duelo_outcome = ['Duelo no Chão Ganho', 'Duelo Aéreo Ganho', 'Duelo no chão perdido', 'Duelo aéreo perdido']

		dicionario_duelo_outcome = {stat: sum(my_df.Nome_Duelo_Outcome == stat) for stat in stats_duelo_outcome}

		# Definindo dicionário para stats da colune index_gol
		stat_index_gol = 1

		dicionario_index_gol = {'Gol': sum(my_df.Index_Gol == stat_index_gol)}

		# Definindo dicionário para stats da coluna index_assistencia
		stat_index_assist = 1

		dicionario_index_assist = {'Assistência': sum(my_df.Index_Assist == stat_index_assist)}

		# Definindo dicionário para stats da coluna index_toque
		stat_index_toque = 1

		dicionario_index_toque = {'Toque': sum(my_df.Index_Toque == stat_index_toque)}

		# Definindo dicionário para stats da coluna index_passe_longo
		stat_index_passe_longo = 1

		dicionario_index_passe_longo = {'Passe Longo': sum(my_df.Index_Passe_Longo == stat_index_passe_longo)}

		# Definindo dicionário para % de passes certos
		lista_percentual_passe_certo = dicionario_pass_outcome['Passe Certo'] / dicionario_nome_ato['Passe']
		lista_percentual_passe_certo = '{:.1%}'.format(lista_percentual_passe_certo)

		dicionario_percent_passes_certo = {'% Passes certos': lista_percentual_passe_certo}

		# Definindo dicionário para % de duelos aéreos ganhos
		lista_percentual_duelos_aereos_vencidos = dicionario_duelo_outcome['Duelo Aéreo Ganho'] / dicionario_nome_duelo['Duelo Aéreo']
		lista_percentual_duelos_aereos_vencidos = '{:.1%}'.format(lista_percentual_duelos_aereos_vencidos)

		dicionario_percent_duelos_aereos_vencidos = {'% Duelos aéreos vencidos': lista_percentual_duelos_aereos_vencidos}

		# Definindo dicionário para % de duelos no chão ganhos
		lista_percentual_duelos_no_chao_vencidos = dicionario_duelo_outcome['Duelo no Chão Ganho'] / dicionario_nome_duelo['Duelo no Chão']
		lista_percentual_duelos_no_chao_vencidos = '{:.1%}'.format(lista_percentual_duelos_no_chao_vencidos)

		dicionario_percent_duelos_no_chao_vencidos = {'% Duelos no chão vencidos': lista_percentual_duelos_no_chao_vencidos}

		# Definindo dicionário gols + assistências
		gols_assistencias = dicionario_index_gol['Gol'] + dicionario_index_assist['Assistência']

		dicionario_gol_assist = {'Gols + Assistências': gols_assistencias}

		# Definindo dicionário classificação média matchday
		dicionario_clas_matchday = {'Classificação média Matchday': 7.9}

		# Juntando os diversos dicionários em um único para o gráfico de evolução
		Dicionario_evolucao = {**dicionario_duelo_outcome, **dicionario_finalizacao_outcome, **dicionario_index_assist,
				       **dicionario_index_gol, **dicionario_index_passe_longo, **dicionario_index_toque,
				       **dicionario_nome_ato, **dicionario_nome_duelo, **dicionario_pass_outcome,
				       **dicionario_percent_duelos_aereos_vencidos, **dicionario_percent_duelos_no_chao_vencidos,
				       **dicionario_percent_passes_certo, **dicionario_gol_assist, **dicionario_clas_matchday}
		
		# Criando selectbox para escolher campeonato
		
		campeonato_escolhido = st.selectbox('Selecione um campeonato', ['FGV Society'])
		
		# Criando figura

		fig, ax = plt.subplots(figsize=(8,24))

	  # Definindo número de linhas e colunas

		cols = 3
		rows = 24

	  # Criar coordenadas com base no número de linhas e colunas

	  # Adicionando bordas

		ax.set_ylim(-1, rows + 1)
		ax.set_xlim(0.25, cols-0.5)

	  # setando a linha inicial

		linha = 24

	  # loop para preencher a tabela chamando as estatísticas

		numero_jogos = len(lista_partidas_selecionaveis)
		
		for stat in stats:
			stat_valor = Dicionario_evolucao[stat]
			if type(stat_valor) != str and stat != 'Classificação média Matchday':
				stat_valor = stat_valor / numero_jogos
			ax.text(x=0.25, y=linha, s=stat+' por partida', va='center', ha='left')
			ax.text(x=2.25, y=linha, s=stat_valor, ha='right')
			linha = linha - 1

	  # colocando cabeçalho
		ax.text(0.25, 24.75, 'Stat', weight='bold', ha='left')
		ax.text(2.25, 24.75, 'Valor', weight='bold', ha='right')
		ax.plot([0.25, cols-0.62], [24.5, 24.5], lw='.5', c='black')

		ax.plot([0.25, cols-0.62], [23.5, 23.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [16.5, 16.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [12.5, 12.5], lw='.2', c='gray')
		ax.plot([0.25, cols-0.62], [5.5, 5.5], lw='.2', c='gray')

	  # tirando eixos
		ax.axis('off')

		fig
	
with tab2:
  
  tab4, tab5 = st.tabs(['Event Map','Heat Map'])
  
  # Desenhando o mapa de passes
  with tab4:
    
  # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

  # Pitch Outline & Centre Line
    ax.plot([0, 0], [0, 25], color="white")
    ax.plot([0, 45], [25, 25], color="white")
    ax.plot([45, 45], [25, 0], color="white")
    ax.plot([45, 0], [0, 0], color="white")
    ax.plot([22.5, 22.5], [0, 25], color="white")

  # Pitch shoot-out lines
    ax.plot([17.5, 17.5], [15, 10], color="white")
    ax.plot([27.5, 27.5], [15, 10], color="white")

  # Left Penalty Area
    ax.plot([8, 8], [20, 5], color="white")
    ax.plot([0, 8], [20, 20], color="white")
    ax.plot([8, 0], [5, 5], color="white")

  # Right Penalty Area
    ax.plot([45, 37], [20, 20], color="white")
    ax.plot([37, 37], [20, 5], color="white")
    ax.plot([37, 45], [5, 5], color="white")

  # Prepare Circles
    centreSpot = plt.Circle((22.5,12.5), 0.1, color="white")
    
  # Draw sentido do campo
    sentido = plt.arrow(18, 26, 8, 0, color="black", head_width = 0.4)
    ax.add_patch(sentido)

  # Draw Circles
    ax.add_patch(centreSpot)

  #Preenchendo de Verde
    plt.fill_between([0,45],[25,25],color="Green", alpha=0.55)

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
        ax.plot([0, 0], [0, 25], color="white")
        ax.plot([0, 45], [25, 25], color="white")
        ax.plot([45, 45], [25, 0], color="white")
        ax.plot([45, 0], [0, 0], color="white")
        ax.plot([22.5, 22.5], [0, 25], color="white")

  # Pitch shoot-out lines
        ax.plot([17.5, 17.5], [15, 10], color="white")
        ax.plot([27.5, 27.5], [15, 10], color="white")

  # Left Penalty Area
        ax.plot([8, 8], [20, 5], color="white")
        ax.plot([0, 8], [20, 20], color="white")
        ax.plot([8, 0], [5, 5], color="white")

  # Right Penalty Area
        ax.plot([45, 37], [20, 20], color="white")
        ax.plot([37, 37], [20, 5], color="white")
        ax.plot([37, 45], [5, 5], color="white")

  # Prepare Circles
        centreSpot = plt.Circle((22.5,12.5), 0.1, color="white")

  # Draw Circles
        ax.add_patch(centreSpot)
    
  # Draw sentido do campo
        sentido = plt.arrow(18, 12.5, 8, 0, color="white", head_width = 0.4)
        ax.add_patch(sentido)

  #Preenchendo de Verde
        ax.fill_between([0,45],[25,25],color="Green", alpha=0.55)

  # Tidy Axes
        ax.axis('off')
  
   # mapa de calor de toques
        customcmap = mat.colors.LinearSegmentedColormap.from_list('custom cmap', ['green', 'yellow','red'])

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
		
		# Puxando o arquivo com a base comparação

		sheet_id = '15Zkt-YrhKGC3JKdPhGl5tjQhaeCfihJiGUev1DKP52o'
		sheet_name = 'Ranking'
		url = 'https://docs.google.com/spreadsheets/d/'+sheet_id+'/gviz/tq?tqx=out:csv&sheet='+sheet_name
		data = pd.read_csv(url)
		data.head()
		
		# Criando select box nome dos jogadores		
		lista_jogadores = ['Samir', 'Lucas', 'Pedro', 'Fernando', 'Luiz', 'João', 'Felipe']
		Jogador1 = st.selectbox('Selecione o primeiro jogador:', lista_jogadores)
		Jogador2 = st.selectbox('Selecione o segundo jogador:', lista_jogadores)
		
		# Criando dataframe para jogadores selecionados
		data_jogador1 = data[(data['Nome_Jogador'] == Jogador1)]
		data_jogador2 = data[(data['Nome_Jogador'] == Jogador2)]
		
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
			if stat_jogador1 > stat_jogador2:
				color1 = 'green'
				alpha1 = 0.1
			else:
				color1 = 'white'
				alpha1 = 0.0
			if stat_jogador2 > stat_jogador1:
				color2 = 'blue'
				alpha2 = 0.1
			else:
				color2 = 'white'
				alpha2 = 0.0
			ax.text(x=0.5, y=linha, s=stat_jogador1, va='center', ha='right', bbox = dict(facecolor=color1, alpha=alpha1))
			ax.text(x=2.25, y=linha, s=stat_jogador2, va='center', ha='right', bbox = dict(facecolor=color2, alpha=alpha2))
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
