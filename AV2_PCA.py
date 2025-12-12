import os
import pandas as pd
nome_arquivo = "inf_alunos.csv"

COLUNAS_COMPLETAS = ["Matricula", "Nome", "Rua", "Numero", "Bairro", "Cidade", "UF", "Telefone", "Email"]
CAMPOS_ALUNO = ["Nome", "Rua", "Numero", "Bairro", "Cidade", "UF", "Telefone", "Email"]

def criar_matricula(df):
  if df.empty:
    return 1
  
  try:
    max_val = df["Matricula"].max()
    if pd.isna(max_val): 
      return 1
    return int(max_val) + 1
  except:
      return len(df) + 1