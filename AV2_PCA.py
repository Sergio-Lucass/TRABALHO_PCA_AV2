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
    try:        
        df = pd.read_csv(nome_arquivo)
        df['Matricula'] = df['Matricula'].astype('Int64')
        
        if 'Matricula' not in df.columns:
          print("Atenção: Coluna 'Matricula' não encontrada. Gerando IDs sequenciais.")
          df.insert(0, 'Matricula', range(1, 1 + len(df)))
            
        return df
         
    except pd.errors.EmptyDataError:
            print(f"\nAtenção: O arquivo '{nome_arquivo}' existe, mas está vazio ou sem colunas. Criando DataFrame vazio.")
            return pd.DataFrame(columns=COLUNAS_COMPLETAS)
            
  else:
    return pd.DataFrame(columns=COLUNAS_COMPLETAS)

def salvar_dados(df):
  df['Matricula'] = df['Matricula'].astype('Int64')
  df.to_csv(nome_arquivo, index=False)
  print("\nDados salvos/atualizados com sucesso!")

def menu_inserir(df):
  print("\n===== INSERIR NOVO ALUNO =====")

  matricula = criar_matricula(df)
  aluno = {}
  aluno["Matricula"] = matricula
  aluno['Nome'] = input("Nome: ").strip()
  aluno['Rua'] = input("Rua: ").strip()
  aluno['Numero'] = input("Número: ").strip()
  aluno['Bairro'] = input("Bairro: ").strip()
  aluno['Cidade'] = input("Cidade: ").strip()
  aluno['UF'] = input("UF (ex: RJ): ").strip().upper()
  aluno['Telefone'] = input("Telefone: ").strip()
  aluno['Email'] = input("E-mail: ").strip()

  df = pd.concat([df, pd.DataFrame([aluno])], ignore_index=True)
  salvar_dados(df)

  print(f"Aluno cadastrado com matrícula {matricula}!\n")
  return df

