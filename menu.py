from dashboard import dashboard
from filabacklog import filabacklog
from pilharecentes import PilhasRecentes
from recomendações import recomendar_jogos
from ranking import gerar_ranking
from registros import registrar_sessao
from carregar_dados import carregar_jogos

def menu():
    lista_jogos = []
    backlog = filabacklog()
    recentes = PilhasRecentes()
    historico = []
    tempo_total = {}

    while True:
        try:
            print("\n" + "="*50)
            print("1. Carregar catálogo")
            print("2. Listar jogos")
            print("3. Buscar jogo por nome")
            print("4. Filtrar por gênero")
            print("5. Filtrar por console")
            print("6. Filtrar por nota")
            print("7. Ordenar catálogo")
            print("8. Adicionar jogo ao backlog")
            print("9. Ver backlog")
            print("10. Jogar próximo do backlog")
            print("11. Ver jogos recentes")
            print("12. Retomar último jogo")
            print("13. Registrar tempo de jogo")
            print("14. Ver histórico completo")
            print("15. Ver recomendações")
            print("16. Ver ranking pessoal")
            print("17. Ver dashboard")
            print("18. Salvar backlog")
            print("19. Sair")
            print("="*50)

            op = input("\nEscolha: ").strip()

            if op == "1":
                print("\nCarregando jogos...")
                lista_jogos = carregar_jogos()
                print(f"✓ {len(lista_jogos)} jogos carregados!")
                
                backlog = filabacklog()
                print("\nPopulando backlog...")
                for jogo in lista_jogos:
                    backlog.enqueue(jogo)
                print(f"✓ Backlog pronto com {backlog.tamanho()} jogos!\n")

            elif op == "2":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    print(f"\nTotal de jogos: {len(lista_jogos)}")
                    print("Primeiros 10 jogos:")
                    for jogo in lista_jogos[:10]:
                        print(f"- {jogo.titulo} ({jogo.console})")

            elif op == "3":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    nome = input("Digite o nome do jogo: ").strip().lower()
                    encontrados = [j for j in lista_jogos if nome in j.titulo.lower()]
                    if encontrados:
                        print(f"\nEncontrados {len(encontrados)} jogo(s):")
                        for jogo in encontrados[:10]:
                            print(f"- {jogo.titulo} ({jogo.console})")
                    else:
                        print("Nenhum jogo encontrado.")

            elif op == "4":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    genero = input("Digite o gênero: ").strip()
                    filtrados = [j for j in lista_jogos if j.genero == genero]
                    if filtrados:
                        print(f"\nEncontrados {len(filtrados)} jogo(s) do gênero '{genero}':")
                        for jogo in filtrados[:10]:
                            print(f"- {jogo.titulo} ({jogo.console})")
                    else:
                        print(f"Nenhum jogo encontrado no gênero '{genero}'.")

            elif op == "5":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    console = input("Digite o console: ").strip()
                    filtrados = [j for j in lista_jogos if j.console == console]
                    if filtrados:
                        print(f"\nEncontrados {len(filtrados)} jogo(s) para '{console}':")
                        for jogo in filtrados[:10]:
                            print(f"- {jogo.titulo} ({jogo.genero})")
                    else:
                        print(f"Nenhum jogo encontrado para '{console}'.")

            elif op == "6":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    try:
                        nota_min = float(input("Digite a nota mínima: "))
                        filtrados = [j for j in lista_jogos if j.critic_score >= nota_min]
                        if filtrados:
                            print(f"\nEncontrados {len(filtrados)} jogo(s) com nota >= {nota_min}:")
                            for jogo in filtrados[:10]:
                                print(f"- {jogo.titulo} ({jogo.critic_score})")
                        else:
                            print(f"Nenhum jogo encontrado com nota >= {nota_min}.")
                    except ValueError:
                        print("Nota inválida!")

            elif op == "7":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    lista_jogos.sort(key=lambda j: j.titulo)
                    print("✓ Catálogo ordenado por título!")

            elif op == "8":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    titulo = input("Digite o título do jogo: ").strip()
                    jogo = next((j for j in lista_jogos if j.titulo.lower() == titulo.lower()), None)
                    if jogo:
                        if not backlog.contem(jogo.id_jogo):
                            backlog.enqueue(jogo)
                            print(f"✓ '{jogo.titulo}' adicionado ao backlog!")
                        else:
                            print("Jogo já está no backlog!")
                    else:
                        print("Jogo não encontrado!")

            elif op == "9":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    print("\n--- VER BACKLOG ---")
                    backlog.mostrar()

            elif op == "10":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    jogo = backlog.dequeue()
                    if jogo:
                        recentes.push(jogo)
                        print("\n==== JOGANDO ====")
                        jogo.exibir()
                        print("================\n")
                    else:
                        print("Backlog vazio! Não há jogos para jogar.")

            elif op == "11":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    recentes.mostrar()

            elif op == "12":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                elif recentes.is_empty():
                    print("Nenhum jogo recente!")
                else:
                    jogo = recentes.topo()
                    print("\n==== RETOMANDO ÚLTIMO JOGO ====")
                    jogo.exibir()
                    try:
                        tempo = float(input("Tempo jogado: "))
                        registrar_sessao(jogo, tempo, historico, tempo_total)
                    except ValueError:
                        print("Tempo inválido!")

            elif op == "13":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                elif recentes.is_empty():
                    print("Nenhum jogo recente para registrar!")
                else:
                    jogo = recentes.topo()
                    try:
                        tempo = float(input("Tempo jogado: "))
                        registrar_sessao(jogo, tempo, historico, tempo_total)
                    except ValueError:
                        print("Tempo inválido!")

            elif op == "14":
                if not historico:
                    print("Histórico vazio!")
                else:
                    print("\n--- HISTÓRICO COMPLETO ---")
                    for i, sessao in enumerate(historico, 1):
                        print(f"{i}. {sessao.jogo.titulo} - {sessao.tempo} horas")

            elif op == "15":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    recomendar_jogos(lista_jogos, historico, tempo_total)

            elif op == "16":
                gerar_ranking(tempo_total)

            elif op == "17":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    dashboard(lista_jogos, backlog, recentes, historico, tempo_total)

            elif op == "18":
                if not lista_jogos:
                    print("Catálogo não carregado!")
                else:
                    with open("backlog.txt", "w", encoding="utf-8") as f:
                        for jogo in backlog.dados:
                            f.write(f"{jogo.titulo},{jogo.console},{jogo.genero}\n")
                    print("Backlog salvo em 'backlog.txt'!")

            elif op == "19":
                print("Saindo...")
                break
            
            else:
                print("Opção inválida!")
        
        except Exception as e:
            print(f"Erro: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    menu()
