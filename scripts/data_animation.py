import numpy as np
import pandas as pd
import output
import pickle


#===========================================
# extract data from .pickle
with open('20191202.pickle',"rb") as f:
            data = pickle.load(f)

traits = data.Microbial_traits
traits.to_csv('traits.csv')

substrates = data.Substrates_C
substrates.to_csv('substrates.csv')

microbes   = data.Microbes_C
microbes.to_csv('microbes.csv')

#============================================
# get portions of data from .csv files

col_index = [10*i for i in range(0,74)]

substrates = pd.read_csv('substrates.csv',index_col=0)
substrates_dense = substrates.iloc[:,col_index]
substrates_dense.to_csv('substrates_dense.csv')

microbes = pd.read_csv('microbes.csv',index_col=0)
microbes_dense = microbes.iloc[:,col_index]
microbes_dense.to_csv('microbes_dense.csv')



# cellulose



substrates_dense = pd.read_csv('substrates_dense.csv',index_col=0)
microbes_dense   = pd.read_csv('microbes_dense.csv',index_col=0)

cellulose = substrates_dense.loc['Cellulose',:]
fungi   = microbes_dense.loc['tax1',:]
bacteria= microbes_dense.loc['tax3',:]

cellulose.to_csv('cellulose.csv')
fungi.to_csv('fungi.csv')
bacteria.to_csv('bacteria.csv')