class Sessao:
    def __init__(self, jogo, tempo):
        self.jogo = jogo
        self.tempo = tempo

historico = []
tempo_total = {}

def registrar_sessao(jogo, tempo, historico_ref, tempo_total_ref):
    sessao = Sessao(jogo, tempo)
    historico_ref.append(sessao)

    if jogo.titulo not in tempo_total_ref:
        tempo_total_ref[jogo.titulo] = 0

    tempo_total_ref[jogo.titulo] += tempo

    print("Sessão registrada!")