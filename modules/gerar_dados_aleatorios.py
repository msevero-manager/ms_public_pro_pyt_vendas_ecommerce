# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  

# Importação da biblioteca random para geração de números aleatórios
import random  

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta  

class gera_dados:

    # Definição da função para gerar dados fictícios de vendas
    def gera_dados_ficticios(num_registros = 600):
        
        """
        Gera um DataFrame do Pandas com os dados de vendas fictícios
        """

        # Mensagem inicial indicando a qtde de registros a serem gerados
        print(f"\nIniciando a geração de {num_registros} registros.")

        # Dicionário com produtos, suas categorias e preços
        produtos = {
            'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
            'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
            'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
            'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
            'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
            'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
            'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
            'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
        }

        # Cria uma lista apenas com os nomes dos produtos
        lista_produtos = list(produtos.keys())

        # Dicionário com cidades e seus respectivos estados
        cidades_estados = {
            'São Paulo': 'SP', 
            'Rio de Janeiro': 'RJ', 
            'Belo Horizonte': 'MG',
            'Porto Alegre': 'RS', 
            'Salvador': 'BA', 
            'Curitiba': 'PR', 
            'Fortaleza': 'CE'
        }

        # Cria uma lista apenas com os nomes das cidades
        lista_cidades = list(cidades_estados.keys())

        # Lista que irá armazenar os registros de vena
        dados_vendas = []

        # Define a data inicial dos pedidos
        data_inicial = datetime(2026, 1, 1)

        # Loop para gerar os registros de vendas
        for i in range(num_registros):

            # Seleciona aleatoriamente um produto
            produto_nome = random.choice(lista_produtos)

            # Seleciona aleatoriamente uma cidade
            cidade = random.choice(lista_cidades)

            # Gera uma quantidade de produtos vendida entre 1 e 7
            quantidade = np.random.randint(1, 8)

            # Calcula a data do pedido a partir da data inicial
            data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0,23))

            # Se o produto for Mouse ou Teclado, aplica desconto
            if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
                preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
            else:
                preco_unitario = produtos[produto_nome]['preco']

            dados_vendas.append({
                'ID_Pedido': 1000 + i,
                'Data_Pedido': data_pedido,
                'Nome_Produto': produto_nome,
                'Categoria': produtos[produto_nome]['categoria'],
                'Preco_Unitario': round(preco_unitario, 2),
                'Quantidade': quantidade,
                'ID_Cliente': np.random.randint(100, 150),
                'Cidade': cidade,
                'Estado': cidades_estados[cidade]
            })

        # Mensagem final indicando que a geração terminou
        print("Geração de dados concluída.\n")

        # Retorna os dados no formato de DataFrame
        return pd.DataFrame(dados_vendas)