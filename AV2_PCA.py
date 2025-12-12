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

def menu_pesquisar(df):
  print("\n===== PESQUISAR ALUNO =====")
  if df.empty:
    print("O cadastro de alunos está vazio.\n")
    return df

  while True:
      try:
          print("Você deseja pesquisar pela matricula ou pelo nome do aluno?")
          print("1 - MATRICULA")
          print("2 - NOME")
          print("3 - VOLTAR PRO MENU")
          print("===========================")
            
          try:
              escolha = int(input("Escolha a opcao: ").strip())
          except ValueError:
              print("Opção inválida. Por favor, digite 1, 2 ou 3.")

          if escolha == 3:
            print("Você retornou para o menu.\n")
            return df
            
          if escolha == 1:
            busca = input("Digite a matrícula: ").strip()
            try:
                busca_int = int(busca)
                resultado = df[df["Matricula"] == busca_int]
            except ValueError:
                print("Matrícula inválida. Digite um número.")
                continue

          elif escolha == 2:
            busca = input("Digite o nome: ").strip().lower()
            resultado = resultado = df[df["Nome"].str.lower() == busca]
            
          else:
            print("Opção inválida!")
            continue
            
          break
        
      except Exception as e:
          print(f"Ocorreu um erro na escolha da pesquisa: {e}")
          continue

  if resultado.empty:
    print("\nNenhum aluno encontrado.\n")
    return df

  aluno_selecionado = None
    
  if len(resultado) > 1:
    print("\n=== MÚLTIPLOS RESULTADOS ENCONTRADOS ===")
    print(resultado[["Matricula", "Nome"]].to_string(index=False))
        
    while True:
      try:
          matricula_selecionada = int(input("Digite a MATRÍCULA do aluno desejado: ").strip())
          aluno_selecionado = resultado[resultado["Matricula"] == matricula_selecionada]

          if not aluno_selecionado.empty:
            break

          else:
            print("Matrícula não encontrada nos resultados.")

      except ValueError:
          print("Matrícula deve ser um número.")

  else:
    aluno_selecionado = resultado

  if aluno_selecionado.empty:
    print("\nSeleção cancelada ou matrícula inválida.")
    return df

  idx = aluno_selecionado.index[0]

  print("\n=== DADOS DO ALUNO SELECIONADO ===")
  print(aluno_selecionado.iloc[0].to_string())
  print("=================================\n")

