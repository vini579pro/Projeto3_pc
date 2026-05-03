def dashboard(lista_jogos, backlog, recentes, historico, tempo_total):

    total_jogos = len(lista_jogos)
    total_backlog = backlog.tamanho()
    total_recentes = recentes.tamanho()
    total_sessoes = len(historico)
    
    tempo_total_geral = sum(tempo_total.values()) if tempo_total else 0
    media_horas_sessao = (tempo_total_geral / total_sessoes) if total_sessoes > 0 else 0

    contagem_status = {"iniciado": 0, "em_andamento": 0, "concluido": 0}
    generos_freq = {}
    consoles_freq = {}
    soma_notas_jogados = 0
    
    melhor_nota_jogo = None
    jogo_mais_popular = None

    for id_jogo, tempo in tempo_total.items():
        jogo_obj = next((j for j in lista_jogos if j.id_jogo == id_jogo), None)
        
        if jogo_obj:
            soma_notas_jogados += jogo_obj.critic_score
            
            generos_freq[jogo_obj.genero] = generos_freq.get(jogo_obj.genero, 0) + 1
            consoles_freq[jogo_obj.console] = consoles_freq.get(jogo_obj.console, 0) + 1
            
            if melhor_nota_jogo is None or jogo_obj.critic_score > melhor_nota_jogo.critic_score:
                melhor_nota_jogo = jogo_obj
            if jogo_mais_popular is None or jogo_obj.total_sales > jogo_mais_popular.total_sales:
                jogo_mais_popular = jogo_obj
            
            if tempo >= 20:
                contagem_status["concluido"] += 1
            elif tempo >= 2:
                contagem_status["em_andamento"] += 1
            else:
                contagem_status["iniciado"] += 1

    genero_favorito = max(generos_freq, key=generos_freq.get) if generos_freq else "sem dados"
    console_favorito = max(consoles_freq, key=consoles_freq.get) if consoles_freq else "sem dados"
    nota_media = (soma_notas_jogados / len(tempo_total)) if tempo_total else 0
    
    id_mais_jogado = max(tempo_total, key=tempo_total.get) if tempo_total else None
    nome_mais_jogado = next((j.titulo for j in lista_jogos if j.id_jogo == id_mais_jogado), "Nenhum")

    print("DASHBOARD")
    
    print(f"Total de jogos no Catálogo:{total_jogos}")
    print(f"Total de jogos no Backlog:{total_backlog}")
    print(f"Total de jogos Recentes:{total_recentes}")
    print(f"Total de sessões jogadas:{total_sessoes}")
    print(f"Tempo total jogado:{tempo_total_geral:.1f} horas")
    print(f"Média de horas por sessão:{media_horas_sessao:.2f} horas")
    print(f"Jogo mais jogado (Tempo):{nome_mais_jogado}")
    print(f"Gênero favorito (Frequência):{genero_favorito}")
    print(f"Console favorito (Frequência):{console_favorito}")
    print(f"Nota média dos jogos jogados:{nota_media:.1f}")
    print(f"Panorama de Progresso:")
    print(f"Jogos Iniciados:{contagem_status['iniciado']}")
    print(f"Jogos em Andamento:{contagem_status['em_andamento']}")
    print(f"Concluídos Simbolicamente:{contagem_status['concluido']}")
    print(f"Destaques do Histórico:")
    print(f"Melhor nota já jogada:{melhor_nota_jogo.titulo if melhor_nota_jogo else 'sem dados'}")
    print(f"Jogo mais popular jogado:{jogo_mais_popular.titulo if jogo_mais_popular else 'sem dados'}")
    
