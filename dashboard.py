def dashboard(lista_jogos, backlog, recentes, historico, tempo_total):
    total_jogos = len(lista_jogos)
    total_backlog = backlog.tamanho()
    total_recentes = recentes.tamanho()
    total_sessoes = len(historico)
    tempo_total_geral = sum(tempo_total.values()) if tempo_total else 0

    jogo_mais_jogado = max(tempo_total, key=tempo_total.get) if tempo_total else "Nenhum"

    print("\nDASHBOARD")
    print(f"Total de jogos: {total_jogos}")
    print(f"Backlog: {total_backlog}")
    print(f"Recentes: {total_recentes}")
    print(f"Sessões: {total_sessoes}")
    print(f"Tempo total jogado: {tempo_total_geral} horas")
    print(f"Jogo mais jogado: {jogo_mais_jogado}")