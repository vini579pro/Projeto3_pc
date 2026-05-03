import csv
from jogo import Jogo

def carregar_jogos(caminho_arquivo='dataset.csv'):
    """Carrega os jogos do arquivo CSV e retorna uma lista de objetos Jogo"""
    jogos = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            id_jogo = 1
            for linha in leitor:
                try:
                    # Converte valores numéricos
                    critic_score = float(linha.get('critic_score', 0)) if linha.get('critic_score') else 0
                    total_sales = float(linha.get('total_sales', 0)) if linha.get('total_sales') else 0
                    na_sales = float(linha.get('na_sales', 0)) if linha.get('na_sales') else 0
                    jp_sales = float(linha.get('jp_sales', 0)) if linha.get('jp_sales') else 0
                    pal_sales = float(linha.get('pal_sales', 0)) if linha.get('pal_sales') else 0
                    other_sales = float(linha.get('other_sales', 0)) if linha.get('other_sales') else 0
                    
                    jogo = Jogo(
                        id_jogo=id_jogo,
                        titulo=linha.get('title', ''),
                        console=linha.get('console', ''),
                        genero=linha.get('genre', ''),
                        publisher=linha.get('publisher', ''),
                        developer=linha.get('developer', ''),
                        critic_score=critic_score,
                        total_vendas=total_sales,
                        vendas_an=na_sales,
                        vendas_jp=jp_sales,
                        vendas_eu=pal_sales,
                        outras_vendas=other_sales,
                        data_lanc=linha.get('release_date', '')
                    )
                    jogos.append(jogo)
                    id_jogo += 1
                except Exception as e:
                    print(f"Erro ao processar linha: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado!")
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
    
    return jogos
