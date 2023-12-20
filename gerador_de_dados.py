import random

# Listas de dados predefinidos
nomes = ['Alice', 'Bob', 'Carol', 'David', 'Eve']
emails = ['alice@example.com', 'bob@example.com',
          'carol@example.com', 'david@example.com', 'eve@example.com']
telefones = ['(11) 99999-1111', '(22) 88888-2222',
             '(33) 77777-3333', '(44) 66666-4444', '(55) 55555-5555']
cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Fortaleza', 'Curitiba']
estados = ['SP', 'RJ', 'BA', 'CE', 'PR']

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
