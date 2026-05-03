def gerar_ranking(tempo_total):
    if not tempo_total:
        print("\nNenhum dado de tempo disponível para gerar o ranking.")
        return

    ranking = sorted(tempo_total.items(), key=lambda x: x[1], reverse=True)

    print("\nRanking de jogos mais jogados:")
    for jogo, tempo in ranking:
        print(jogo, "-", tempo, "horas")