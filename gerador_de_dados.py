import random

# Listas de dados predefinidos
nomes = ['João Silva', 'Maria Oliveira', 'Carlos Santos', 'Ana Souza', 'Pedro Ferreira']
emails = ['joao.silva@gmail.com', 'maria.oliveira@hotmail.com',
          'carlos.santos@outlook.com', 'ana.souza@yahoo.com', 'pedro.ferreira@uol.com.br']
telefones = ['(11) 91234-5678', '(21) 92345-6789',
             '(31) 93456-7891', '(41) 94567-8912', '(51) 95678-9123']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
estados = ['SP', 'RJ', 'MG', 'PR', 'RS']

# Função para gerar os dados aleatórios


def gerar_dados(escolhas):
    resultado = {
        'nome': random.choice(nomes) if '1' in escolhas else '',
        'email': random.choice(emails) if '2' in escolhas else '',
        'telefone': random.choice(telefones) if '3' in escolhas else '',
        'cidade': random.choice(cidades) if '4' in escolhas else '',
        'estado': random.choice(estados) if '5' in escolhas else '',
    }
    return resultado

# Função para salvar os dados em um arquivo


def salvar_arquivo(dados):
    with open('dados.txt', 'a') as arquivo:
        linha = ' '.join(filter(None, dados.values()))
        arquivo.write(linha + '\n')


# Interface do programa
while True:
    print("\nOpções de dados a serem gerados:")
    print("1 - Gerar nome")
    print("2 - Gerar e-mail")
    print("3 - Gerar telefone")
    print("4 - Gerar cidade")
    print("5 - Gerar estado")
    print("Digite 'parar' para finalizar o programa.")
    print("Escolha uma ou mais opções separadas por espaço (ex: 1 3 5):")
    escolha_usuario = input()

    if escolha_usuario.lower() == 'parar':
        print("Programa finalizado.")
        break

    escolhas = escolha_usuario.split()
    dados_gerados = gerar_dados(escolhas)
    for chave, valor in dados_gerados.items():
        if valor:
            print(f"{chave.capitalize()}: {valor}")

    salvar_no_arquivo = input("Deseja salvar os dados em um arquivo (s/n)? ")
    if salvar_no_arquivo.lower() == 's':
        salvar_arquivo(dados_gerados)
    else:
        continue
