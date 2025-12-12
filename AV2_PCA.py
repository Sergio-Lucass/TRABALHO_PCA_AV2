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
  
def carregar_dados():
  if os.path.exists(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    df['Matricula'] = df['Matricula'].astype('Int64')
        
  if 'Matricula' not in df.columns:
    print("Atenção: Coluna 'Matricula' não encontrada. Gerando IDs sequenciais.")
    df.insert(0, 'Matricula', range(1, 1 + len(df)))
    return df
  
  else:
    return pd.DataFrame(columns=COLUNAS_COMPLETAS)

def salvar_dados(df):
    df['Matricula'] = df['Matricula'].astype('Int64')
    df.to_csv(nome_arquivo, index=False)
    print("\nDados salvos/atualizados com sucesso!")

