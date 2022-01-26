# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:47:25 2021


RECOMENDADO PYTHON 2
@author: Vitor
"""
import pandas as pd
import numpy as np
threshold=175
missing=-9999
"""
CARREGAR OS ARQUIVOS DA ESTAÇÃO
"""
parati1=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2009_A_31-12-2009.csv",encoding='latin-1')
parati2=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2010_A_31-12-2010.csv",encoding='latin-1')
parati3=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2011_A_31-12-2011.csv",encoding='latin-1')
parati4=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2012_A_31-12-2012.csv",encoding='latin-1')
parati5=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2013_A_31-12-2013.csv",encoding='latin-1')
parati6=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2014_A_31-12-2014.csv",encoding='latin-1')
parati7=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2015_A_31-12-2015.csv",encoding='latin-1')
parati8=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2016_A_31-12-2016.csv",encoding='latin-1')
parati9=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2017_A_31-12-2017.csv",encoding='latin-1')
parati10=pd.read_csv("INMET_SE_RJ_A619_PARATI_01-01-2018_A_31-12-2018.csv",encoding='latin-1')
"""
JUNTAR OS DADOS DA ESTAÇÃO EM UM ARQUIVO SÓ
"""
paratifull=pd.concat([parati1,parati2,parati3,parati4,parati5,parati6,parati7,parati8,parati9,parati10]).reset_index()
paratifull["DATA (YYYY-MM-DD)"]=pd.to_datetime(paratifull["DATA (YYYY-MM-DD)"],format='%d/%m/%Y')
paratifull["HORA (UTC)"] = paratifull["HORA (UTC)"] + ':00'
paratifull["HORA (UTC)"]=pd.to_timedelta(paratifull["HORA (UTC)"],unit="m")
paratifull["DATA (YYYY-MM-DD)"]=paratifull["DATA (YYYY-MM-DD)"]+paratifull["HORA (UTC)"]


paratifull=paratifull.drop(["HORA (UTC)"],axis=1)
paratifull=paratifull.drop(["index"],axis=1)
paratifull=paratifull.rename(columns={"DATA (YYYY-MM-DD)": 'local time', paratifull.columns[6]: 'air temp mean', paratifull.columns[7]:'dew point mean',"VENTO. VELOCIDADE HORARIA (m/s)":'wind speed mean', paratifull.columns[5]:'ghi mean'})
paratifull.loc[paratifull['ghi mean'] == -9999, 'ghi mean'] = 0
paratifull["month"]=paratifull["local time"].dt.to_period("M")
paratifull["n_missing"]=(paratifull.groupby("month")['air temp mean'].transform(lambda d:(d==missing).sum()))
paratifull['air temp mean']=np.where((paratifull['air temp mean']==missing) & (paratifull["n_missing"]>threshold),np.nan,paratifull['air temp mean'])
paratifull['air temp mean']=np.where((paratifull['air temp mean']==missing) & (paratifull["n_missing"]<threshold),0,paratifull['air temp mean'])
paratifull["n_missing"]=(paratifull.groupby("month")['dew point mean'].transform(lambda d:(d==missing).sum()))
paratifull['dew point mean']=np.where((paratifull['dew point mean']==missing) & (paratifull["n_missing"]>threshold),np.nan,paratifull['dew point mean'])
paratifull['dew point mean']=np.where((paratifull['dew point mean']==missing) & (paratifull["n_missing"]<threshold),0,paratifull['dew point mean'])
paratifull["n_missing"]=(paratifull.groupby("month")['wind speed mean'].transform(lambda d:(d==missing).sum()))
paratifull['wind speed mean']=np.where((paratifull['wind speed mean']==missing) & (paratifull["n_missing"]>threshold),np.nan,paratifull['wind speed mean'])
paratifull['wind speed mean']=np.where((paratifull['wind speed mean']==missing) & (paratifull["n_missing"]<threshold),0,paratifull['wind speed mean'])
paratifull.to_csv("INMET_SE_RJ_A619_PARATI_JUNTO_01-01-2009_A_31-12-2018.csv",encoding='latin-1')




