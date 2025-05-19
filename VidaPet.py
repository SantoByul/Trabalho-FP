import datetime
import os
pets_list = []
portes_validos = ["pequeno", "medio", "grande"]
opcoes_petshop = {
    "1": "Unidade Boa Viagem",
    "2": "Unidade Espinheiro",
    "3": "Unidade Caxangá",
    "4": "Unidade Recife Antigo"
}
def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)
def adicionarpet():
    nome = input("Nome do pet: ").lower()
    if not nome:
        print("Você não inseriu um nome.")
        return
    especie = input("Espécie: ").lower()
    if not especie:
        print("Você não inseriu uma espécie.")
        return
    porte = input("Seu animal é de porte pequeno, médio ou grande?: ").lower()
    if porte not in portes_validos:
        print("Você só pode escolher entre pequeno, médio e grande.")
        return
    nascimento = input("Data de nascimento: ")
    if not nascimento:
        print("Você não inseriu uma data de nascimento.")
        return
    peso = input("Peso(kg): ")
    if not peso:
        print("Você não inseriu um peso.")
        return
    with open("pets.txt", "a") as arquivo:
        arquivo.write(f"{nome};{especie};{porte};{nascimento};{peso}\n")
    pets_list.append(nome)
    print("Pet cadastrado.")
    print("Lista dos seus pets:", pets_list)
def visualizarpet():
    try:
        if not arquivo_existe("pets.txt"):
            print("Nenhum pet cadastrado.")
            return

        with open("pets.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:  # Verifica se o arquivo está vazio
                print("Não há conteúdo no arquivo para ser visualizado.")
                return

            for linha in sorted(linhas):
                partes = linha.strip().split(";")
                if len(partes) == 5:
                    nome, especie, porte, nascimento, peso = partes
                    print(f"Nome: {nome} | Espécie: {especie} | Porte: {porte} | Nascimento: {nascimento} | Peso: {peso}kg")
                else:
                    print(f"[⚠️ Linha inválida ignorada]: {linha.strip()}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum pet cadastrado.")
def editarpet():
    nome_pet = input("Digite o nome do pet que deseja editar: ")
    if not arquivo_existe("pets.txt"):
        print("Arquivo de pets não encontrado.")
        return
    pets = []
    encontrado = False
    with open("pets.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.startswith(nome_pet + ";"):
                print("Digite os novos dados:")
                nome = input("Novo nome: ")
                especie = input("Nova espécie: ")
                porte = input("Novo porte: ")
                nascimento = input("Nova data de nascimento: ")
                peso = input("Novo peso: ")
                pets.append(f"{nome};{especie};{porte};{nascimento};{peso}\n")
                encontrado = True
            else:
                pets.append(linha)

    if encontrado:
        with open("pets.txt", "w") as arquivo:
            arquivo.writelines(pets)
        print("Pet atualizado com sucesso!")
    else:
        print("Pet não encontrado.")
def excluirpet():
    nome_pet = input("Digite o nome do pet que deseja excluir: ")
    if not arquivo_existe("pets.txt"):
        print("Arquivo de pets não encontrado.")
        return
    pets = []
    excluido = False
    with open("pets.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.startswith(nome_pet + ";"):
                excluido = True
            else:
                pets.append(linha)
    if excluido:
        with open("pets.txt", "w") as arquivo:
            arquivo.writelines(pets)
        print(f"Pet {nome_pet} excluído.")
    else:
        print("Pet não encontrado.")
def registrarevento():
    if nome == None : 
        print ("você não tem pets cadastrados")
    data = input("Data do evento: ")
    nome_pet = input("Nome do pet: ")
    tipo_evento = input("Tipo de evento (vacina, consulta, remédio): ").lower()
    observacoes = input("Observações: ")
    with open("eventos.txt", "a") as arquivo:
        arquivo.write(f"{data};{nome_pet};{tipo_evento};{observacoes}\n")
    print("Evento registrado.")

def exibireventos():
    if not arquivo_existe("eventos.txt"):
        print("Nenhum evento registrado.")
        return
    with open("eventos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            data, nome_pet, tipo, obs = linha.strip().split(";")
            print(f"Data: {data} | Pet: {nome_pet} | Tipo: {tipo} | Obs: {obs}")

def definirmeta():
    descricao = input("Descrição da meta: ")
    frequencia = input("Frequência: ")
    with open("metas.txt", "a") as arquivo:
        arquivo.write(f"{descricao};{frequencia}\n")
    print("Meta registrada.")

def exibirmetas():
    if not arquivo_existe("metas.txt"):
        print("Nenhuma meta definida.")
        return
    with open("metas.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            descricao, frequencia = linha.strip().split(";")
            print(f"Meta: {descricao} | Frequência: {frequencia}")

def cumprirmeta():
    descricao = input("Digite a descrição exata da meta que você cumpriu: ")
    data = datetime.datetime.now().strftime("%d/%m/%Y")
    with open("cumprimentos.txt", "a") as arquivo:
        arquivo.write(f"{descricao};{data}\n")
    print("Cumprimento registrado.")
def verificarcumprimento():
    if not arquivo_existe("metas.txt"):
        print("Nenhuma meta registrada.")
        return
    with open("metas.txt", "r") as arquivo:
        linhas_metas = arquivo.readlines()
        metas = [linha.strip().split(";")[0] for linha in linhas_metas]

    registros = []
    if arquivo_existe("cumprimentos.txt"):
        with open("cumprimentos.txt", "r") as arquivo:
            linhas_cumprimentos = arquivo.readlines()
            registros = [linha.strip().split(";")[0] for linha in linhas_cumprimentos]

    for meta in metas:
        vezes = registros.count(meta)
        print(f"Meta: {meta} | Cumprimentos registrados: {vezes}")

def sugestoescuidados():
    especie = input("Espécie do pet (cachorro/gato): ").lower()
    idade = float(input("Idade do pet (em anos, use número com vírgula se necessário): ").replace(',', '.'))
    porte = input("Porte do pet (pequeno/médio/grande): ").lower()

    if especie == "cachorro":
        if idade < 1:
            print("• Vacinação completa")
            print("• Rações específicas para filhotes")
            print("• Visitas ao veterinário a cada 2 a 3 meses")
            print("• Brinquedos para dentição")
        else:
            print("• Alimentação equilibrada com ração para adultos")
            print("• Consultas veterinárias a cada 6 meses")
            print("• Atividades físicas regulares")
            if porte == "pequeno":
                print("• Caminhadas curtas diárias")
                print("• Cuidados com o frio (roupas, caminhas quentes)")
            elif porte == "medio":
                print("• Exercícios moderados")
                print("• Espaço razoável para se movimentar")
            elif porte == "grande":
                print("• Exercícios intensos e caminhadas longas")
                print("• Acesso a áreas abertas e maiores")
            else:
                print("Porte não reconhecido. Informe pequeno, médio ou grande.")

    elif especie == "gato":
        if idade < 1:
            print("• Brinquedos leves e seguros")
            print("• Caixa de areia acessível")
            print("• Ração para filhotes")
            print("• Vacinação completa")
        else:
            print("• Ração específica para adultos")
            print("• Escovação regular (principalmente se peludo)")
            print("• Sessões de brincadeiras interativas")
            if porte == "pequeno":
                print("• Brinquedos pequenos e acessíveis")
            elif porte == "medio":
                print("• Arranhadores de tamanho médio")
            elif porte == "grande":
                print("• Espaço vertical (prateleiras, torres)")
                print("• Monitoramento do peso")
            else:
                print("Porte não reconhecido. Informe pequeno, médio ou grande.")
    else:
        print("Espécie não reconhecida. Informe 'cachorro' ou 'gato'.")

def escolher_petshop_proximo():
    print("\n--- Escolha o Petshop Mais Próximo ---")
    for chave, nome_petshop in opcoes_petshop.items():
        print(f"{chave}. {nome_petshop}")

    while True:
        opcao = input("Digite o número do petshop desejado: ")
        if opcao in opcoes_petshop:
            petshop_escolhido = opcoes_petshop[opcao]
            print(f"Você escolheu: {petshop_escolhido}")
            break
        else:
            print("Opção inválida. Por favor, digite um número da lista.")

while True:
    print("\n--- VIDA PET ---")
    print("1. Adicionar Pet")
    print("2. Visualizar Pets")
    print("3. Editar Pet")
    print("4. Excluir Pet")
    print("5. Registrar Evento")
    print("6. Exibir Eventos")
    print("7. Definir Meta de Saúde")
    print("8. Exibir Metas")
    print("9. Cumprir Meta")
    print("10. Verificar Cumprimento de Metas")
    print("11. Sugestões de Cuidados")
    print("12. Escolher Petshop Próximo")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionarpet()
    elif opcao == "2" : 
        visualizarpet()
    elif opcao == "3":
        editarpet()
    elif opcao == "4":
        excluirpet()
    elif opcao == "5":
        registrarevento()
    elif opcao == "6":
        exibireventos()
    elif opcao == "7":
        definirmeta()
    elif opcao == "8":
        exibirmetas()
    elif opcao == "9":
        cumprirmeta()
    elif opcao == "10":
        verificarcumprimento()
    elif opcao == "11":
        sugestoescuidados()
    elif opcao == "12":
        escolher_petshop_proximo()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")


def limpar_arquivo_pets():
    open("pets.txt", "w").close()
    print("Arquivo de pets limpo.")
