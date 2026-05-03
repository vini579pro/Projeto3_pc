def recomendar_jogos(lista_jogos, historico, tempo_total):
    generos = {}

    for sessao in historico:
        jogo = getattr(sessao, "jogo", None)
        if jogo is None:
            continue

        genero = getattr(jogo, "genero", None)
        if genero is None:
            continue

        generos[genero] = generos.get(genero, 0) + 1

    if not generos:
        print("Sem dados para recomendação")
        return

    genero_favorito = max(generos, key=generos.get)

    recomendados = [
        jogo for jogo in lista_jogos
        if getattr(jogo, "genero", None) == genero_favorito
        and jogo.titulo not in tempo_total
    ]

    if not recomendados:
        print("Nenhuma recomendação disponível")
        return

    print("\nRecomendações:")
    for jogo in recomendados[:10]:
        print(jogo.titulo)