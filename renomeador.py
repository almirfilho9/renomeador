import os

# Defina o diretório onde os arquivos estão localizados
directory = r"caminho/do/seu/diretorio"

# Lista de nomes para renomear os arquivos
names = [
    "Nome 1",
    "Nome 2",
    "Nome 3",
    # Adicione mais nomes conforme necessário
]

# Muda o diretório de trabalho
os.chdir(directory)

# Loop para renomear os arquivos
for i, name in enumerate(names, start=1):
    # Formato do nome do arquivo original
    original_file = f"arquivo_original_{str(i).zfill(2)}.jpg"  # Exemplo: arquivo_original_01.jpg
    # Novo nome do arquivo
    new_file = f"{name}.jpg"
    
    # Verifica se o arquivo original existe
    if os.path.exists(original_file):
        # Verifica se o novo arquivo já existe
        if not os.path.exists(new_file):
            os.rename(original_file, new_file)
            print(f"Renomeado: {original_file} para {new_file}")
        else:
            print(f"Arquivo {new_file} já existe. Não foi renomeado.")
    else:
        print(f"Arquivo {original_file} não encontrado.")
