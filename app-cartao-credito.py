# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AshpJ1hABK7qtGsJhJ7XHmFSuuLI4oIo
"""


#para o streamlit
#--------BIBLIOTECAS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


#--------LENDO ARQUIVO
arquivo = pd.read_csv('card_transdata.csv', sep=',')
#classificação de transação legítima==0 e fraudulenta==1
nomesClassesED=['LEGÍTIMO', 'FRAUDE']

#--------SEPARANDO COLUNAS
colunas = arquivo.columns.to_list()
nomesColunas = colunas [:7]
dataset_features = arquivo[nomesColunas]
dataset_classes = arquivo['fraud']

#--------DIVISÃO DOS DADOS DE TREINO E TESTE
feature_treino,feature_teste,classes_treino,classes_teste = train_test_split(dataset_features,
                                                                             dataset_classes,
                                                                             test_size=0.25,
                                                                             random_state=12)

#--------CONSTRUÇÃO DA ARVORE
arvore = DecisionTreeClassifier()
arvore.fit(feature_treino,classes_treino)
predicao = arvore.predict(feature_teste)

import streamlit as st

st.number_input('Distância entre a casa do cliente e lugar de transação: ', key='distCasa')
st.number_input('Distância entre a transação atual com a última transação: ', key='distTransacoes')
st.number_input('Proporção da transação do preço de compra para o preço de compra mediano: ', key='precoMedio')
st.number_input'A transação é com o mesmo varejista? ', key='varejista')
st.number_input('A transação  é feita com cartão de crédito? ', key='cartaoCredito')
st.number_input('A transação é feita com cartão PIN de cartão de crédito? ', key='pin')
st.number_input(' A transação é online?', key='online')



individuo = [st.session_state.distCasa,st.session_state.distTransacoes,
             st.session_state.precoMedio,st.session_state.varejista,
             st.session_state.cartaoCredito, st.session_state.pin, st.session_state.online]

if st.button('Analisar'):
  predicao = arvore.predict([individuo])
  st.write('O animal previsto pela árvore é: '+nomes_classes[int(predicao[0])])
