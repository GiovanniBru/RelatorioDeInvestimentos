# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 00:45:50 2021

@author: Giovanni
"""

import pandas as pd


data = pd.read_excel('fff.xlsx')

#dt = pd.DataFrame(data=dataset[:,5,9,12,13])

dropcolumns = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 
               'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8',
               'Unnamed: 10', 'Unnamed: 11']
#dropcolumns = ['COD_FILIAL']
try:
  data = data.drop(dropcolumns, axis = 1)
except Exception as e:
    print(e)
    
data.dropna(inplace=True)

#data = data[["Produto", "Agencia", "Data", "Valor"]]

data = data.drop(data.index[0])

# d2 = data.rename(columns={'Unnamed 5':'Produto'})

data['Unnamed: 12'] = pd.to_datetime(data['Unnamed: 12'], format='%d/%m%Y')

data.info()

# Separar por ano 
data['ANO'] = data['Unnamed: 12'].dt.year


dropcolumns = ['Unnamed: 12']
#dropcolumns = ['COD_FILIAL']
try:
  data = data.drop(dropcolumns, axis = 1)
except Exception as e:
    print(e)
    

# Relacionar Produto e Valor Anualmente 
    
data_12 = data.loc[(data['ANO'] == 2012)]

data_13 = data.loc[(data['ANO'] == 2013)]

data_14 = data.loc[(data['ANO'] == 2014)]

data_15 = data.loc[(data['ANO'] == 2015)]

data_16 = data.loc[(data['ANO'] == 2016)]

data_17 = data.loc[(data['ANO'] == 2017)]

data_18 = data.loc[(data['ANO'] == 2018)]

data_19 = data.loc[(data['ANO'] == 2019)]

data_20 = data.loc[(data['ANO'] == 2020)]

# 2012: 
total12 = data_12['Unnamed: 13'].sum()
    # 2.716.661,60
print(pd.unique(data['Unnamed: 5']))

data12_out = data_12.loc[(data_12['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')] # 253.650
data12_jor = data_12.loc[(data_12['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]  # 113550
data12_rad = data_12.loc[(data_12['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total12_RAD = data12_rad['Unnamed: 13'].sum()   # 679.819,05
data12_tv = data_12.loc[(data_12['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total12_tv = data12_tv['Unnamed: 13'].sum()     # 1.653.853,08
data12_prod = data_12.loc[(data_12['Unnamed: 5'] == 'PRODUÇÃO')]    # 15.789,5


# 2013 
total13 = data_13['Unnamed: 13'].sum()      # 143.052.917,64
    #OUTDOOR
data13_out = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total13_out = data13_out['Unnamed: 13'].sum()   # 473,535.0
    #JORNAL
data13_jor = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total13_jor = data13_jor['Unnamed: 13'].sum()   # 3.599.435,26
    # RADIO 
data13_rad = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total13_rad = data13_rad['Unnamed: 13'].sum()   # 32.968.494,2
    # TV
data13_tv = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total13_tv = data13_tv['Unnamed: 13'].sum()     # 63.166.899,45
    # PRODUCAO
data13_prod = data_13.loc[(data_13['Unnamed: 5'] == 'PRODUÇÃO')]
total13_prod = data13_prod['Unnamed: 13'].sum() # 32.030.130,94
    # CRIAÇÃO
data13_cri = data_13.loc[(data_13['Unnamed: 5'] == 'CRIAÇÃO')]
total13_cri = data13_cri['Unnamed: 13'].sum()   # 1.947.957,49
    # VEICULAÇÃO - REVISTA
data13_rev = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total13_rev = data13_rev['Unnamed: 13'].sum()   # 940.224,89
    # VEICULAÇÃO - PORTAL
data13_pt = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total13_pt = data13_pt['Unnamed: 13'].sum()     # 6.454.015,95
    # VEICULAÇÃO - OUTROS
data13_otr = data_13.loc[(data_13['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total13_otr = data13_otr['Unnamed: 13'].sum()   # 1.472.224,46


# 2014 
total14 = data_14['Unnamed: 13'].sum()      # 8.284.939,54
    #OUTDOOR
data14_out = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total14_out = data14_out['Unnamed: 13'].sum()   # 163.352,5
    #JORNAL
data14_jor = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total14_jor = data14_jor['Unnamed: 13'].sum()   # 56.857,5
    # RADIO 
data14_rad = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total14_rad = data14_rad['Unnamed: 13'].sum()   # 2.454.238,08
    # TV
data14_tv = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total14_tv = data14_tv['Unnamed: 13'].sum()     # 302.227,3
    # PRODUCAO
data14_prod = data_14.loc[(data_14['Unnamed: 5'] == 'PRODUÇÃO')]
total14_prod = data14_prod['Unnamed: 13'].sum() # 3.754.350,09
    # CRIAÇÃO
data14_cri = data_14.loc[(data_14['Unnamed: 5'] == 'CRIAÇÃO')]
total14_cri = data14_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data14_rev = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total14_rev = data14_rev['Unnamed: 13'].sum()   # 212.575
    # VEICULAÇÃO - PORTAL
data14_pt = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total14_pt = data14_pt['Unnamed: 13'].sum()     # 1.131.843,32
    # VEICULAÇÃO - OUTROS
data14_otr = data_14.loc[(data_14['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total14_otr = data14_otr['Unnamed: 13'].sum()   # 209.495,75


# 2015
total15 = data_15['Unnamed: 13'].sum()      # 11.948.143,58
    #OUTDOOR
data15_out = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total15_out = data15_out['Unnamed: 13'].sum()   # 112.100
    #JORNAL
data15_jor = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total15_jor = data15_jor['Unnamed: 13'].sum()   # 17.575
    # RADIO 
data15_rad = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total15_rad = data15_rad['Unnamed: 13'].sum()   # 615.785,23
    # TV
data15_tv = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total15_tv = data15_tv['Unnamed: 13'].sum()     # 1.920.710,15
    # PRODUCAO
data15_prod = data_15.loc[(data_15['Unnamed: 5'] == 'PRODUÇÃO')]
total15_prod = data15_prod['Unnamed: 13'].sum() # 6.820.146,1
    # CRIAÇÃO
data15_cri = data_15.loc[(data_15['Unnamed: 5'] == 'CRIAÇÃO')]
total15_cri = data15_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data15_rev = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total15_rev = data15_rev['Unnamed: 13'].sum()   # 359.724,34
    # VEICULAÇÃO - PORTAL
data15_pt = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total15_pt = data15_pt['Unnamed: 13'].sum()     # 1.649.470,51
    # VEICULAÇÃO - OUTROS
data15_otr = data_15.loc[(data_15['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total15_otr = data15_otr['Unnamed: 13'].sum()   # 452.632,25


# 2016 
total16 = data_16['Unnamed: 13'].sum()      # 7.637.570,97
    #OUTDOOR
data16_out = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total16_out = data16_out['Unnamed: 13'].sum()   # 34.295
    #JORNAL
data16_jor = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total16_jor = data16_jor['Unnamed: 13'].sum()   # 4.750
    # RADIO 
data16_rad = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total16_rad = data16_rad['Unnamed: 13'].sum()   # 1.106.261,58
    # TV
data16_tv = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total16_tv = data16_tv['Unnamed: 13'].sum()     # 194.002,35
    # PRODUCAO
data16_prod = data_16.loc[(data_16['Unnamed: 5'] == 'PRODUÇÃO')]
total16_prod = data16_prod['Unnamed: 13'].sum() # 4.400.613,11
    # CRIAÇÃO
data16_cri = data_16.loc[(data_16['Unnamed: 5'] == 'CRIAÇÃO')]
total16_cri = data16_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data16_rev = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total16_rev = data16_rev['Unnamed: 13'].sum()   # 198.668,75
    # VEICULAÇÃO - PORTAL
data16_pt = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total16_pt = data16_pt['Unnamed: 13'].sum()     # 1.614.411,05
    # VEICULAÇÃO - OUTROS
data16_otr = data_16.loc[(data_16['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total16_otr = data16_otr['Unnamed: 13'].sum()   # 84.569,13


# 2017
total17 = data_17['Unnamed: 13'].sum()      # 19.563.213,5
    #OUTDOOR
data17_out = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total17_out = data17_out['Unnamed: 13'].sum()   # 19.855
    #JORNAL
data17_jor = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total17_jor = data17_jor['Unnamed: 13'].sum()   # 110.157,33
    # RADIO 
data17_rad = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total17_rad = data17_rad['Unnamed: 13'].sum()   # 3.431.934,97
    # TV
data17_tv = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total17_tv = data17_tv['Unnamed: 13'].sum()     # 6.854.925,06
    # PRODUCAO
data17_prod = data_17.loc[(data_17['Unnamed: 5'] == 'PRODUÇÃO')]
total17_prod = data17_prod['Unnamed: 13'].sum() # 7.960.451,42
    # CRIAÇÃO
data17_cri = data_17.loc[(data_17['Unnamed: 5'] == 'CRIAÇÃO')]
total17_cri = data17_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data17_rev = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total17_rev = data17_rev['Unnamed: 13'].sum()   # 619.432,98
    # VEICULAÇÃO - PORTAL
data17_pt = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total17_pt = data17_pt['Unnamed: 13'].sum()     # 489.919,37
    # VEICULAÇÃO - OUTROS
data17_otr = data_17.loc[(data_17['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total17_otr = data17_otr['Unnamed: 13'].sum()   # 76.537,37


# 2018
total18 = data_18['Unnamed: 13'].sum()      # 8.028.400,023
    #OUTDOOR
data18_out = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total18_out = data18_out['Unnamed: 13'].sum()   # 262.935
    #JORNAL
data18_jor = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total18_jor = data18_jor['Unnamed: 13'].sum()   # 232.573,41
    # RADIO 
data18_rad = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total18_rad = data18_rad['Unnamed: 13'].sum()   # 1.740.449,54
    # TV
data18_tv = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total18_tv = data18_tv['Unnamed: 13'].sum()     # 27.930
    # PRODUCAO
data18_prod = data_18.loc[(data_18['Unnamed: 5'] == 'PRODUÇÃO')]
total18_prod = data18_prod['Unnamed: 13'].sum() # 4.419.757,59
    # CRIAÇÃO
data18_cri = data_18.loc[(data_18['Unnamed: 5'] == 'CRIAÇÃO')]
total18_cri = data18_cri['Unnamed: 13'].sum()   # 107.987,46
    # VEICULAÇÃO - REVISTA
data18_rev = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total18_rev = data18_rev['Unnamed: 13'].sum()   # 28.203,12
    # VEICULAÇÃO - PORTAL
data18_pt = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total18_pt = data18_pt['Unnamed: 13'].sum()     # 769.918,8
    # VEICULAÇÃO - OUTROS
data18_otr = data_18.loc[(data_18['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total18_otr = data18_otr['Unnamed: 13'].sum()   # 438.645,11


# 2019 
total19 = data_19['Unnamed: 13'].sum()      # 4.845.223,59
    #OUTDOOR
data19_out = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total19_out = data19_out['Unnamed: 13'].sum()   # 94.912,5
    #JORNAL
data19_jor = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total19_jor = data19_jor['Unnamed: 13'].sum()   # 71.203,26
    # RADIO 
data19_rad = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total19_rad = data19_rad['Unnamed: 13'].sum()   # 1.119.707,77
    # TV
data19_tv = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total19_tv = data19_tv['Unnamed: 13'].sum()     # 283.955
    # PRODUCAO
data19_prod = data_19.loc[(data_19['Unnamed: 5'] == 'PRODUÇÃO')]
total19_prod = data19_prod['Unnamed: 13'].sum() # 1.671.659,07
    # CRIAÇÃO
data19_cri = data_19.loc[(data_19['Unnamed: 5'] == 'CRIAÇÃO')]
total19_cri = data19_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data19_rev = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total19_rev = data19_rev['Unnamed: 13'].sum()   # 48.925
    # VEICULAÇÃO - PORTAL
data19_pt = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total19_pt = data19_pt['Unnamed: 13'].sum()     # 1.462.682,64
    # VEICULAÇÃO - OUTROS
data19_otr = data_19.loc[(data_19['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total19_otr = data19_otr['Unnamed: 13'].sum()   # 92.178,35


# 2020 
total20 = data_20['Unnamed: 13'].sum()      # 1.232.949,28
    #OUTDOOR
data20_out = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - OUTDOOR')]
total20_out = data20_out['Unnamed: 13'].sum()   # 15.030
    #JORNAL
data20_jor = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - JORNAL')]
total20_jor = data20_jor['Unnamed: 13'].sum()   # 0
    # RADIO 
data20_rad = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - RADIO')]
total20_rad = data20_rad['Unnamed: 13'].sum()   # 116.327,85
    # TV
data20_tv = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - TV')]
total20_tv = data20_tv['Unnamed: 13'].sum()     # 0
    # PRODUCAO
data20_prod = data_20.loc[(data_20['Unnamed: 5'] == 'PRODUÇÃO')]
total20_prod = data20_prod['Unnamed: 13'].sum() # 667.350,65
    # CRIAÇÃO
data20_cri = data_20.loc[(data_20['Unnamed: 5'] == 'CRIAÇÃO')]
total20_cri = data20_cri['Unnamed: 13'].sum()   # 0
    # VEICULAÇÃO - REVISTA
data20_rev = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - REVISTA')]
total20_rev = data20_rev['Unnamed: 13'].sum()   # 1.000
    # VEICULAÇÃO - PORTAL
data20_pt = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - PORTAL')]
total20_pt = data20_pt['Unnamed: 13'].sum()     # 404.740,78
    # VEICULAÇÃO - OUTROS
data20_otr = data_20.loc[(data_20['Unnamed: 5'] == 'VEICULAÇÃO - OUTROS')]
total20_otr = data20_otr['Unnamed: 13'].sum()   # 28.500


total = data['Unnamed: 13'].sum()   # 207.310.019,73


# relacionar agência e valor, anualmente
print(pd.unique(data['Unnamed: 9']))
'''
['Antares Publicidade Ltda'
 'Sin Comunicação Ltda'
 'Artfinal de Propaganda Ltda'
 'Mix Com Agencia de Propaganda e Publicidade Ltda'
 'Faz Comunicacao Ltda - EPP' 
 'Real Publicidade Ltda'
 'Takes Produção e Publicidade Ltda' 
 'Maxima Tres Comunicacao Ltda-ME'
 'MART PET COMUNICAÇÃO LTDA - EPP']
'''

# 2012
total12 = data_12['Unnamed: 13'].sum()
    # 2.716.661,60

data12_ant = data_12.loc[(data_12['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data12_ant['Unnamed: 13'].sum())   # 645.104,45

data12_sin = data_12.loc[(data_12['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data12_sin['Unnamed: 13'].sum())   # 1.735.117,98

data12_art = data_12.loc[(data_12['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data12_art['Unnamed: 13'].sum())      # 15.789,47

data12_mix = data_12.loc[(data_12['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data12_mix['Unnamed: 13'].sum())  # 13.632,5

data12_faz = data_12.loc[(data_12['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data12_faz['Unnamed: 13'].sum())  # 307.017,2

data12_real = data_12.loc[(data_12['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data12_real['Unnamed: 13'].sum())     # 0 

data12_tk = data_12.loc[(data_12['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data12_tk['Unnamed: 13'].sum())   # 0 

data12_max = data_12.loc[(data_12['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data12_max['Unnamed: 13'].sum())  # 0 

data12_mt = data_12.loc[(data_12['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data12_mt['Unnamed: 13'].sum())   # 0 


# 2013 
total13 = data_13['Unnamed: 13'].sum()      # 143.052.917,64

data13_ant = data_13.loc[(data_13['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data13_ant['Unnamed: 13'].sum())   # 49.475.722,5

data13_sin = data_13.loc[(data_13['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data13_sin['Unnamed: 13'].sum())   # 19.576.313,64

data13_art = data_13.loc[(data_13['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data13_art['Unnamed: 13'].sum())      # 1.242.928,65

data13_mix = data_13.loc[(data_13['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data13_mix['Unnamed: 13'].sum())  # 9.263.052,54

data13_faz = data_13.loc[(data_13['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data13_faz['Unnamed: 13'].sum())  # 13.413.776,2

data13_real = data_13.loc[(data_13['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data13_real['Unnamed: 13'].sum())     # 8.232.254,38

data13_tk = data_13.loc[(data_13['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data13_tk['Unnamed: 13'].sum())   # 14.589.273,53

data13_max = data_13.loc[(data_13['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data13_max['Unnamed: 13'].sum())  # 27.259.596,20

data13_mt = data_13.loc[(data_13['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data13_mt['Unnamed: 13'].sum())   # 0 


# 2014 
total14 = data_14['Unnamed: 13'].sum()      # 8.284.939,54

data14_ant = data_14.loc[(data_14['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data14_ant['Unnamed: 13'].sum())   # 1.188.859,63

data14_sin = data_14.loc[(data_14['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data14_sin['Unnamed: 13'].sum())   # 954.734,34

data14_art = data_14.loc[(data_14['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data14_art['Unnamed: 13'].sum())      # 456.722,5

data14_mix = data_14.loc[(data_14['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data14_mix['Unnamed: 13'].sum())  # 462.139,8

data14_faz = data_14.loc[(data_14['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data14_faz['Unnamed: 13'].sum())  # 2.422.640,5

data14_real = data_14.loc[(data_14['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data14_real['Unnamed: 13'].sum())     # 365.540,31

data14_tk = data_14.loc[(data_14['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data14_tk['Unnamed: 13'].sum())   # 952.899,54

data14_max = data_14.loc[(data_14['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data14_max['Unnamed: 13'].sum())  # 1.481.402,92

data14_mt = data_14.loc[(data_14['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data14_mt['Unnamed: 13'].sum())   # 0 

# 2015
total15 = data_15['Unnamed: 13'].sum()      # 11.948.143,58

data15_ant = data_15.loc[(data_15['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data15_ant['Unnamed: 13'].sum())   # 2.158.591,66

data15_sin = data_15.loc[(data_15['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data15_sin['Unnamed: 13'].sum())   # 1.343.693,9

data15_art = data_15.loc[(data_15['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data15_art['Unnamed: 13'].sum())      # 2.034.943,65

data15_mix = data_15.loc[(data_15['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data15_mix['Unnamed: 13'].sum())  # 0

data15_faz = data_15.loc[(data_15['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data15_faz['Unnamed: 13'].sum())  # 512.098,85

data15_real = data_15.loc[(data_15['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data15_real['Unnamed: 13'].sum())     # 305.444,99

data15_tk = data_15.loc[(data_15['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data15_tk['Unnamed: 13'].sum())   # 1.288.362,70

data15_max = data_15.loc[(data_15['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data15_max['Unnamed: 13'].sum())  # 4.305.007,83

data15_mt = data_15.loc[(data_15['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data15_mt['Unnamed: 13'].sum())   # 0 


# 2016 
total16 = data_16['Unnamed: 13'].sum()      # 7.637.570,97

data16_ant = data_16.loc[(data_16['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data16_ant['Unnamed: 13'].sum())   # 3.790.208,55

data16_sin = data_16.loc[(data_16['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data16_sin['Unnamed: 13'].sum())   # 242.754,3

data16_art = data_16.loc[(data_16['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data16_art['Unnamed: 13'].sum())      # 119.040,36

data16_mix = data_16.loc[(data_16['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data16_mix['Unnamed: 13'].sum())  # 2.003.446,13

data16_faz = data_16.loc[(data_16['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data16_faz['Unnamed: 13'].sum())  # 12.500

data16_real = data_16.loc[(data_16['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data16_real['Unnamed: 13'].sum())     # 580.408

data16_tk = data_16.loc[(data_16['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data16_tk['Unnamed: 13'].sum())   # 521.312,27

data16_max = data_16.loc[(data_16['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data16_max['Unnamed: 13'].sum())  # 367.901,36

data16_mt = data_16.loc[(data_16['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data16_mt['Unnamed: 13'].sum())   # 0


# 2017
total17 = data_17['Unnamed: 13'].sum()      # 19.563.213,5

data17_ant = data_17.loc[(data_17['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data17_ant['Unnamed: 13'].sum())   # 773.051,04

data17_sin = data_17.loc[(data_17['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data17_sin['Unnamed: 13'].sum())   # 23.346,25

data17_art = data_17.loc[(data_17['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data17_art['Unnamed: 13'].sum())      # 0

data17_mix = data_17.loc[(data_17['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data17_mix['Unnamed: 13'].sum())  # 0

data17_faz = data_17.loc[(data_17['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data17_faz['Unnamed: 13'].sum())  # 54.145

data17_real = data_17.loc[(data_17['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data17_real['Unnamed: 13'].sum())     # 90.874

data17_tk = data_17.loc[(data_17['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data17_tk['Unnamed: 13'].sum())   # 3.087.583,53

data17_max = data_17.loc[(data_17['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data17_max['Unnamed: 13'].sum())  # 1.897.968,89

data17_mt = data_17.loc[(data_17['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data17_mt['Unnamed: 13'].sum())   # 13.636.244,79

# 2018
total18 = data_18['Unnamed: 13'].sum()      # 8.028.400,023

data18_ant = data_18.loc[(data_18['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data18_ant['Unnamed: 13'].sum())   # 2.044.532,44

data18_sin = data_18.loc[(data_18['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data18_sin['Unnamed: 13'].sum())   # 3.744,9

data18_art = data_18.loc[(data_18['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data18_art['Unnamed: 13'].sum())      # 0

data18_mix = data_18.loc[(data_18['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data18_mix['Unnamed: 13'].sum())  # 12.825

data18_faz = data_18.loc[(data_18['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data18_faz['Unnamed: 13'].sum())  # 0

data18_real = data_18.loc[(data_18['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data18_real['Unnamed: 13'].sum())     # 32.812,5

data18_tk = data_18.loc[(data_18['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data18_tk['Unnamed: 13'].sum())   # 2.702.578,17

data18_max = data_18.loc[(data_18['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data18_max['Unnamed: 13'].sum())  # 2.455.560,71

data18_mt = data_18.loc[(data_18['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data18_mt['Unnamed: 13'].sum())   # 776.346,31


# 2019 
total19 = data_19['Unnamed: 13'].sum()      # 4.845.223,59

data19_ant = data_19.loc[(data_19['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data19_ant['Unnamed: 13'].sum())   # 1.022.207,79

data19_sin = data_19.loc[(data_19['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data19_sin['Unnamed: 13'].sum())   # 0

data19_art = data_19.loc[(data_19['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data19_art['Unnamed: 13'].sum())      # 0

data19_mix = data_19.loc[(data_19['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data19_mix['Unnamed: 13'].sum())  # 0

data19_faz = data_19.loc[(data_19['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data19_faz['Unnamed: 13'].sum())  # 0

data19_real = data_19.loc[(data_19['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data19_real['Unnamed: 13'].sum())     # 0

data19_tk = data_19.loc[(data_19['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data19_tk['Unnamed: 13'].sum())   # 973.113,94

data19_max = data_19.loc[(data_19['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data19_max['Unnamed: 13'].sum())  # 1.365.967,71

data19_mt = data_19.loc[(data_19['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data19_mt['Unnamed: 13'].sum())   # 1.483.934,15

# 2020 
total20 = data_20['Unnamed: 13'].sum()      # 1.232.949,28

data20_ant = data_20.loc[(data_20['Unnamed: 9'] == 'Antares Publicidade Ltda')] 
print(data20_ant['Unnamed: 13'].sum())   # 162.418,67

data20_sin = data_20.loc[(data_20['Unnamed: 9'] == 'Sin Comunicação Ltda')]  
print(data20_sin['Unnamed: 13'].sum())   # 0

data20_art = data_20.loc[(data_20['Unnamed: 9'] == 'Artfinal de Propaganda Ltda')]  
print(data20_art['Unnamed: 13'].sum())      # 0

data20_mix = data_20.loc[(data_20['Unnamed: 9'] == 'Mix Com Agencia de Propaganda e Publicidade Ltda')]  
print(data20_mix['Unnamed: 13'].sum())  # 0

data20_faz = data_20.loc[(data_20['Unnamed: 9'] == 'Faz Comunicacao Ltda - EPP')]  
print(data20_faz['Unnamed: 13'].sum())  # 0

data20_real = data_20.loc[(data_20['Unnamed: 9'] == 'Real Publicidade Ltda')]  
print(data20_real['Unnamed: 13'].sum())     # 0

data20_tk = data_20.loc[(data_20['Unnamed: 9'] == 'Takes Produção e Publicidade Ltda')]  
print(data20_tk['Unnamed: 13'].sum())   # 130.120,74

data20_max = data_20.loc[(data_20['Unnamed: 9'] == 'Maxima Tres Comunicacao Ltda-ME')]  
print(data20_max['Unnamed: 13'].sum())  # 473.488,99

data20_mt = data_20.loc[(data_20['Unnamed: 9'] == 'MART PET COMUNICAÇÃO LTDA - EPP')]  
print(data20_mt['Unnamed: 13'].sum())   # 466.920,88



